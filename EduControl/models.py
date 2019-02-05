from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfileInfo(models.Model):
    # includes: username, email, password
    GENDER_CHOICES= (
        ('M', 'Male'),
        ('F'. 'Female')
    )

    user = models.OneToOneField(User)

    FirstName = models.CharField(max_length=255)
    LastName = models.CharField(max_length=255)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    country = models.CharField(max_length=36)
    city = models.CharField(max_length=36)

    def __str__(self):
        return self.user.username
