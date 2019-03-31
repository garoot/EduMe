from django.db import models
from phone_field import PhoneField
from django.contrib.auth.models import AbstractBaseUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from django import forms

# Create your models here.
class Instructor(AbstractBaseUser):
    FirstName = models.CharField(max_length=255)
    LastName = models.CharField(max_length=255)
    InstructorEmail = models.EmailField(max_length=255, unique=True)
    BirthDate = models.DateField()
    PhoneNumber = PhoneField()
    Country = models.CharField(max_length=255)
    City = models.CharField(max_length=255)
    #for now we'll use CharField for Address
    Address = models.CharField(max_length=255)
    UserStatus = models.BooleanField('user_status', default=False)
    InstructorStatus = models.BooleanField('instructor status', default=False)


    USERNAME_FIELD = 'InstructorEmail'

    def __str__(self):
        return self.InstructorEmail

    def create_instructor_courses_list():
        InstructorCourses = InstructorCourses.objects.create(self.id)

#the signal function below to be removed to a seperate signals.py file later
#the function below is triggered when an instance of Instructor model is created
@receiver(post_save, sender=Instructor)
def is_instructor_created(sender, instance, created, **kwargs):
    if created:
        InstructorCourses.objects.create(instructor_id = instance)
    else:
        instance.InstructorCourses.save()
#######################################################################
class InstructorCourses(models.Model):
    instructor_id = models.OneToOneField(Instructor, on_delete=models.CASCADE, related_name= 'CoursesList')
