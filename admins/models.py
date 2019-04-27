from django.db import models
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model

# Create your models here.

class Category(models.Model):
    category=models.CharField(max_length=255)

    def __str__(self):
        return self.category

class Subcategory(models.Model):
    category=models.ForeignKey(Category, on_delete=models.SET_NULL, related_name="subcategories")
    subcategory=models.CharField(max_length=255)

    def __str__(self):
        return self.subcategory
