from django.db import models
# from courses.models import Course
# from courses.models import Course
# from django.contrib.auth.models import profile
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model

# Course = apps.get_model('courses','Course')

User = get_user_model()
# Create your models here.
EDUCATION_DEGREES =(
    ('None', 'None'),
    ('D', 'Diploma'),
    ('B', 'Bachelor\'s Degree'),
    ('M', 'Master\'s Degree'),
    ('PH', 'PhD'),
)
APPLICATION_STATUS=(
    ('none', 'None'),
    ('submitted', 'Submitted'),
    ('accepted', 'Accepted'),
    ('rejected', 'Rejected')
)


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
        Profile.objects.get_or_create(user=instance)

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name = 'profile')
    country = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=254, blank=True)
    nationality = models.CharField(max_length=255, blank=True)
    dob = models.DateField(blank=True, null=True, verbose_name="Date of Birth")
    """
    The following boolean fields to be controlled by admins and not to be shown to profiles:
        - is_student field will be True in all cases
        - is_instructor & is_promoter will be False by default and once application is approved, admins change it to True
    """
    is_student = models.BooleanField(default=True)
    is_instructor = models.BooleanField(default=False)
    is_promoter = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    """
    the variable below keeps track of the status of the most recent application
    """
    instructor_application_status = models.CharField(max_length=5, choices=APPLICATION_STATUS, default='None')

    """
    the image files below will be stored in folder 'user' followed by the date it is saved
    """
    photo = models.ImageField(upload_to='users/%Y/%m/%d', null=True, blank=True)

    def __str__(self):
        return 'Profile of the user {}'.format(self.user.username)

    """
    this function return true if the application should show up to a user or not
    under two conditions:
    1-  instructor_application_status = 'rejected' or
    2- instructor_application_status = 'None'
    """
    def show_instructor_application(self):
        if self.instructor_application_status == 'rejected' or self.instructor_application_status == 'none':
            return True
        else:
            return False

@receiver(post_save, sender=Profile)
def create_course_list(sender, instance, created, **kwargs):

    if instance.is_instructor:
        InstructorCoursesList.objects.get_or_create(profile=instance)
    else:
        print("is_instructor is False")
@receiver(post_save, sender=Profile)
def create_student(sender, instance, created, **kwargs):
    """
    This must always be true because all profiles must be students
    """
    if instance.is_student:
        WishList.objects.get_or_create(profile = instance)
        PurchaseList.objects.get_or_create(profile = instance)
        PaymentInfo.objects.get_or_create(profile = instance)
        """
        the following model must be created for all students as they might apply to become instructors
        """
        try:
            InstructorResume.objects.get_or_create(profile = instance)
        except InstructorResume.MultipleObjectsReturned:
            print("Exception ERROR: multiple objects returned!")
    else:
        print("is_student is False, change the field to True")


@receiver(post_save, sender=Profile)
def create_instructor(sender, instance, created, **kwargs):
    print('****', created)
    if instance.is_instructor:
        InstructorBankingInfo.objects.get_or_create(profile = instance)
        InstructorCoursesList.objects.get_or_create(profile = instance)
        InstructorReport.objects.get_or_create(profile = instance)
    else:
        print("profile is not instructor")



# @receiver(post_save, sender=Profile)
# def create_promoter(sender, instance, created, **kwargs):
#     if instance.is_promoter:
#         PromoterProfile.objects.get_or_create(profile = instance)
#         """
#         since all promoters are students by default, we will run the following line of code anyway
#         """
#         StudentProfile.objects.get_or_create(profile = instance)
#
#     else:
#         print("profile is not promoter")
"""
- WishList and WishListCourse are the classes related to the wish list tables
- Only WishList will be automatically created once a profile is created
"""
class WishList(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name='wish_list')
class WishListCourse(models.Model):
    wish_list = models.ForeignKey(WishList, on_delete=models.CASCADE, related_name='courses')
    course = models.ForeignKey('courses.Course', on_delete=models.CASCADE)
"""
"""

"""
- PurchaseList and PurchasedCourse are the classes related to the purchasing process
- Only PurchaseList will be automatically created once a profile is created
"""
class PurchaseList(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name='purchase_list')
class PurchasedCourse(models.Model):
    purchase_list = models.ForeignKey(PurchaseList, on_delete=models.CASCADE, related_name='purchased_course')
    course = models.ForeignKey('courses.Course', on_delete=models.CASCADE)
"""
"""

"""
- Below are classes related tothe payment process
- PaymentInfo will be automatically created once a profile is created
"""
class PaymentInfo(models.Model):
    profile = models.OneToOneField(Profile,on_delete=models.CASCADE, related_name='payment_info')
"""
- This is automatically created once PaymentInfo is create_student
- profile can also add as many CardPaymentInfo as needed
"""
class CardPaymentInfo(models.Model):
    payment_info = models.ForeignKey(PaymentInfo, on_delete=models.CASCADE, related_name='card_info')
    full_name = models.CharField(max_length=255)
    card_number = models.IntegerField()
    expriy_date = models.DateField()
    security_number = models.IntegerField()
"""
- This is automatically created once PaymentInfo is create_student
"""
class PayPalInfo(models.Model):
    payment_info = models.OneToOneField(PaymentInfo, on_delete=models.CASCADE, related_name='paypal_info')
    profilename = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
"""
"""

"""
Instructor-related classes

They will all be automatically created if the is_instructor field of the profile is True
"""
class InstructorResume(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='instructor_qualification')
    degree = models.CharField(max_length=2, choices=EDUCATION_DEGREES, default='None')
    major = models.CharField(max_length=344)
    experience = models.TextField(help_text= 'Briefly, describe your background knowledge related to the topics you want to teach')
    status = models.CharField(max_length=5, choices=APPLICATION_STATUS, default='None')


class InstructorBankingInfo(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name = 'banking_info')
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    address = models.CharField(max_length=455)
    """
    below is just a temporary field and will be chnged once payment system is configured
    """
    banking_info = models.CharField(max_length=455)

class InstructorCoursesList(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, blank=True, related_name='course_lists')

"""
This will be automatically created once the InstructorInfo is created
"""
class InstructorReport(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, null=True, related_name='report')
    instructor_revenue = models.FloatField(max_length=200,  null=True)
    number_of_students = models.IntegerField(null=True)
    rating = models.FloatField(null=True)
