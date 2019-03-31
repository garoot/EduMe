from django.contrib import admin
from .models import Instructor, InstructorCourses

# Register your models here.
admin.site.register(Instructor)
admin.site.register(InstructorCourses)
