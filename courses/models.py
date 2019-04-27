from django.db import models
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from accounts.models import InstructorReport, InstructorCoursesList, Profile

class Category(models.Model):
    category=models.CharField(max_length=255)

    def __str__(self):
        return self.category

class Subcategory(models.Model):
    category=models.ForeignKey(Category, on_delete=models.CASCADE, related_name="subcategories")
    subcategory=models.CharField(max_length=255)

    def __str__(self):
        return self.subcategory
# Create your models here.
class Course(models.Model):
    instructor_course_list = models.ForeignKey(InstructorCoursesList, on_delete=models.SET_NULL, related_name="courses", null=True)
    course_name = models.CharField(max_length=255)
    course_topic = models.CharField(max_length=255)
    course_price = models.FloatField()
    course_title = models.CharField(max_length=255)
    course_outline = models.TextField()
    course_requirements = models.TextField()
    course_outcomes = models.TextField()
    course_description = models.TextField()
    target_students = models.TextField()
    # should be uploaded to a folder related to images of course of the same category
    course_picture = models.FileField(upload_to="")
    course_category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name="courses", null=True)
    course_subcategory = models.ForeignKey(Subcategory, on_delete=models.SET_NULL, related_name="courses", null=True)
    course_rating = models.FloatField()

class CourseSection(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="sections")
    section_num = models.IntegerField()
    section_name = models.CharField(max_length = 255, blank=True)

class ContentBase(models.Model):
    course_section = models.ForeignKey(CourseSection, on_delete=models.CASCADE, related_name="item")
    title = models.CharField(max_length=455)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title

class File(ContentBase):
    """
    before this line, we must identify the course category because..
    ..files will be saved into different folders based on that
    """
    course_section = models.ForeignKey(CourseSection, on_delete=models.CASCADE, related_name="files")
    file = models.FileField(upload_to="")
class Video(ContentBase):
    course_section = models.ForeignKey(CourseSection, on_delete=models.CASCADE, related_name="videos")
    file = models.FileField(upload_to="")

class Image(ContentBase):
    course_section = models.ForeignKey(CourseSection, on_delete=models.CASCADE, related_name="images")
    file = models.FileField(upload_to="")

# AKA cart
class Order(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='order_lists')
    """
    - Purchase date is automatically adjusted to "today's date" upon the completion of a purchase
    - It will be copied to the payment information email
    - it's not to be adjusted by customers
    """
    purchase_date = models.DateTimeField(auto_now_add=True, blank=True)
    """
    - Total amount is instantly updated when a course is added or removed from the list
    """
    total_amount = models.FloatField(blank=True)


class CourseReport(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="reports")
    course_rating = models.FloatField(blank=True)
    num_visitors = models.IntegerField(blank=True)
    num_buyers = models.IntegerField(blank=True)
    course_revenue = models.FloatField(blank=True)
    """
    the course report is linked to the instructor's report instantly
    """
    instructor_report = models.ForeignKey(InstructorReport, on_delete=models.SET_NULL, related_name="course_report", null=True)

"""
When the user adds a course to the order list, OrderItem is created
"""
class OrderItem(models.Model):
    order_list = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    """
    - when a course is added to the order list, we check if the promotion code field is valid
    - Then based on the promotion we adjust the price of the order item
    - Then we update the total price of the order
    """
    purchase_price =models.FloatField(blank=True)
    colurse_report = models.ForeignKey(CourseReport, on_delete=models.SET_NULL, related_name="order_item", null=True)
