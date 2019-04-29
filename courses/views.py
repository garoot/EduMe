from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from .forms import CourseInfoForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from accounts.models import InstructorCoursesList, Profile
from .models import Course, CourseSection, CourseReport, Video, File, OrderItem, Order, Image, Category, Subcategory
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your views here.
app_name = 'courses'

@login_required
def create_course(request):
    profile = Profile(user=request.user)
    course_list = InstructorCoursesList(profile=profile)
    course = Course(instructor_course_list=course_list)

    if request.method == 'POST':
        new_course_form = CourseInfoForm(instance=course, data=request.POST, files=request.FILES)
        if new_course_form.is_valid():
            new_course_form.save()
        else:
            messages.error(request, 'error creating the course')
    else:
        print("here...")
        new_course_form = CourseInfoForm()
    return render(request, 'courses/create_course.html', {'new_course_form':new_course_form})
