from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.db.models.signals import post_save



# Create your models here.
class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_instructor = models.BooleanField(default=False)
    is_promoter = models.BooleanField(default=False)
    email = models.EmailField(max_length=100,unique=True)
    #YYYY-MM-DD format
    # birthdate = models.DateField(max_length=16, blank=True)
    # USERNAME_FIELD = 'username'
class InstructorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='instructor_profile')
    country = models.CharField(max_length=32, blank=True)
    city = models.CharField(max_length=32, blank=True)
    degree = models.CharField(max_length=255, blank=True)
    major = models.CharField(max_length=100, blank=True)
    is_approved = models.BooleanField(default=False)

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='student_profile')

#if new user chooses to be a promoter, promoter profile is made but will still needs approval
#   to create the related tables (related tables will be covered in later phases)
class PromoterProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='promoter_profile')
    is_approved = models.BooleanField(default=False)

@receiver(post_save, sender=User)
def create_instructor_data(sender, instance, created, **kwargs):
    print('****', created)
    if instance.is_instructor:
        InstructorProfile.objects.get_or_create(user = instance)

    elif instance.is_student:
        StudentProfile.objects.get_or_create(user = instance)


    elif instance.is_promoter:
        PromoterProfile.objects.get_or_create(user = instance)

    else:
        print("User type is not set..")

@receiver(post_save, sender=InstructorProfile)
def create_instructor_banking(sender, instance, created, **kwargs):
    if instance.is_approved:
        InstructorBankingInfo.objects.get_or_create(user = instance)
        InstructorCourses.objects.get_or_create(user = instance)
        InstructorReport.objects.get_or_create(user = instance)
    else:
        print("Instructor is not approved...")

class InstructorCourses(models.Model):
    instructor = models.OneToOneField(InstructorProfile, on_delete=models.CASCADE, null=True, related_name='courses')

class InstructorBankingInfo(models.Model):
    instructor = models.OneToOneField(InstructorProfile, on_delete=models.CASCADE, null=True, related_name='banking_info')
    branch = models.CharField(max_length=255, default = '')
    institution_number = models.IntegerField()
    iban = models.IntegerField()

#instructor report is to track the  data in the fields below
class InstructorReport(models.Model):
    instructor = models.OneToOneField(InstructorProfile, on_delete=models.CASCADE, null=True, related_name='report')
    instructor_revenue = models.FloatField(max_length=200, blank=True)
    number_of_students = models.IntegerField(blank=True)
    rating = models.FloatField(blank=True)
