from django.contrib import admin
from .models import User, InstructorProfile

# Register your models here.
admin.site.register(User)
admin.site.register(InstructorProfile)
