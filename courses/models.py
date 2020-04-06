from django.db import models
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.utils import timezone
from django.apps import apps
from django.core.exceptions import ObjectDoesNotExist



CATEGORIES =(
    ('0', 'Science'),
    ('1', 'Math & Algebra'),
    ('2', 'Development'),
    ('none', 'None'),
    )
SUBCATEGORIES=(
    ('0', 'Web Development'),
    ('1', 'Calculus I'),
    ('2', 'Programming'),
    ('none', 'None'),
    )
COURSE_LEVELS=(
    ('0', 'Beginner'),
    ('1', 'Intermediate'),
    ('2', 'Advanced'),
    )
CONTENT_TYPE=(
    ('video', 'Video'),
    ('image', 'Image'),
    ('file', 'File'),
    )
COURSE_TYPES=(
    ('none', 'None'),
    ('academic', 'Academic Learning'),
    ('practical', 'Practical Learning'),
    ('tech', 'Tech-Related Courses'),
    ('theory', 'Theoretical Learning'),
)
class Category(models.Model):
    name=models.CharField(max_length=255, default="", unique=True)

    def __str__(self):
        return self.name
"""
must change attribute 'subcategory' to 'name'
"""
class Subcategory(models.Model):
    category=models.ForeignKey(Category, on_delete=models.CASCADE, related_name="subcategories")
    subcategory=models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.subcategory
# Create your models here.

class Course(models.Model):
    # instructor_course_list = models.ForeignKey('accounts.InstructorCoursesList', on_delete=models.SET_NULL, related_name="courses", null=True)
    course_name = models.CharField(max_length=255, verbose_name='Name of the Course')
    course_topic = models.CharField(max_length=255)
    course_price = models.FloatField(null=True)
    course_title = models.CharField(max_length=255)
    course_outline = models.TextField()
    course_requirements = models.TextField()
    course_level = models.CharField(max_length=3, choices=COURSE_LEVELS, default="None")
    course_outcomes = models.TextField()
    course_description = models.TextField()
    target_students = models.TextField()
    # should be uploaded to a folder related to images of course of the same category
    course_picture = models.ImageField(upload_to='courses/%Y/%m/%d', null=True)
    course_category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name="courses", null=True)
    # course_category = models.CharField(max_length=3, choices=CATEGORIES, default="None")
    course_subcategory = models.CharField(max_length=6, choices=SUBCATEGORIES, default="None")

    # course_subcategory = models.ForeignKey(Subcategory, on_delete=models.SET_NULL, related_name="courses", null=True)
    course_type = models.CharField(max_length=25, choices=COURSE_TYPES, default="None")
    course_rating = models.FloatField(null=True)
    #course_length is automatically calculated when the course is created
    course_length = models.FloatField(null=True)
    created = models.DateTimeField(default=timezone.now, editable=False)
    updated = models.DateTimeField(auto_now=True)
    #if a course is discounted, no promo code can apply to any OrderItem
    discounted = models.BooleanField(default=False)

    def __str__(self):
        return self.course_name

class CourseSection(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="sections", null=True)
    section_num = models.IntegerField(null=True)
    section_name = models.CharField(max_length = 255, blank=True)
    created = models.DateTimeField(default=timezone.now, editable=False)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.section_name

class ContentItem(models.Model):
    course_section = models.ForeignKey(CourseSection, on_delete=models.CASCADE, related_name="files")
    title = models.CharField(max_length=455)
    created = models.DateTimeField(default=timezone.now, editable=False)
    updated = models.DateTimeField(auto_now=True)
    content_type = models.CharField(max_length=10, choices=CONTENT_TYPE, default="None")
    file = models.FileField(upload_to='courses/contents/%Y/%m/%d')

    def __str__(self):
        return self.title

    def get_id(self):
        return self.id

class CourseReport(models.Model):
    course = models.OneToOneField(Course, on_delete=models.CASCADE, related_name="report")
    rating = models.FloatField(default=0)
    num_visitors = models.IntegerField(default=0)
    num_buyers = models.IntegerField(default=0)
    course_revenue = models.FloatField(default=0)
    """
    the course report is linked to the instructor's report instantly
    """
    # instructor_report = models.ForeignKey('accounts.InstructorReport', on_delete=models.SET_NULL, related_name="course_report", null=True)

    def add_rating(self, new_rating):
        if self.num_buyers == 0:
            self.num_buyers += 1
            self.rating = new_rating
        elif self.num_buyers != 0:
            self.num_buyers += 1
        self.rating = (self.rating + new_rating) / 2
        return self.rating

    def update_revenue(self, purchase_amount):
        self.course_revenue += purchase_amount

    def update_num_buyers(self):
        self.num_buyers += 1

    def update_num_visitors(self):
        self.num_visitors += 1

# class PromotionCode(models.Model):
#     course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="promo_codes")
#     code = models.CharField(max_length=10, unique=True, primary_key=True )
#     valid_from = models.DateTimeField()
#     valid_to = models.DateTimeField()
#     active = models.BooleanField()
#     uses = models.IntegerField(null=True)

# class Order(models.Model):
#     profile = models.ForeignKey('accounts.Profile', on_delete=models.CASCADE, related_name='orders')

#     """
#     - Purchase date is automatically adjusted to "today's date" upon the completion of a purchase
#     - It will be copied to the payment information email
#     - it's not to be adjusted by customers
#     """
#     purchase_date = models.DateTimeField(default=timezone.now, editable=False, blank=True)
#     """
#     - Total amount is instantly updated when a course is added or removed from the list
#     """
#     total_amount = models.FloatField(blank=True)


"""
When the user adds a course to the order list, OrderItem is created
"""
# class OrderItem(models.Model):
#     order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="order_items")
#     course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
#     """
#     - when a course is added to the order list, we check if the promotion code field is valid
#     - Then based on the promotion we adjust the price in the cart and the order item
#     - Then we update the total price of the order
#     """
#     purchase_price =models.FloatField(blank=True)
#     course_report = models.ForeignKey(CourseReport, on_delete=models.SET_NULL, related_name="report_items", null=True)

#     def update_purchase_price(discount_amount):
#         self.purchase_price = course.course_price - discount_amount

@receiver(post_save, sender=Course)
def create_course_report(sender, instance, created, **kwargs):
        CourseReport.objects.get_or_create(course=instance)
