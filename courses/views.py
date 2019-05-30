from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from .forms import CourseInfoForm,CourseSectionForm, CourseSectionFormSet, ContentFormSet, ContentForm
from django.contrib.auth.decorators import login_required
from django.apps import apps
from django.contrib import messages
from accounts.models import InstructorCoursesList, Profile
from .models import Course, CourseSection, CourseReport, ContentItem, OrderItem, Order, Category, Subcategory
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your views here.

def index(request):
    return render(request, 'EduMe/index.html')

def display_course_page(request, course_id):
    try:
        course = Course.objects.filter(id=course_id)[0]

    except Course.MultipleObjectsReturned:
        print("Exception ERROR: multiple objects returned!")

    return render(request, 'courses/contents/course_page.html', {'course':course})

def display_catalog(request, category=None, subcategory=None, type=None):
    category_obj = None
    print("Category: {}".format(category))
    if category==None :
        try:
            courses = Course.objects.all()
        except Course.MultipleObjectsReturned:
            print("Exception ERROR: multiple objects returned!")
        subcategory = None

    if category:
        print("Passed category condition")

        try:
            category_obj = Category.objects.filter(id=category)[0]
            print("Category: {}".format(category_obj.name))
        except Category.MultipleObjectsReturned:
            print("Exception ERROR: multiple objects returned!")

        try:
            courses = Course.objects.filter(course_category=category_obj)
        except Course.MultipleObjectsReturned:
            print("Exception ERROR: multiple objects returned!")

    if subcategory:
        try:
            subcategory_obj = Subcategory.objects.filter(subcategory=subcategory)[0]
        except Subcategory.MultipleObjectsReturned:
            print("Exception ERROR: multiple objects returned!")

        try:
            courses = Course.objects.all().filter(course_subcategory=subcategory_obj)
        except Course.MultipleObjectsReturned:
            print("Exception ERROR: multiple objects returned!")

    try:
        categories = Category.objects.all()
    except Category.MultipleObjectsReturned:
        print("Exception ERROR: multiple objects returned!")

    try:
        subcategories = Subcategory.objects.all()
    except Subcategory.MultipleObjectsReturned:
        print("Exception ERROR: multiple objects returned!")

    return render(request, 'courses/shop/catalog.html', {'courses':courses, 'categories':categories, 'subcategories':subcategories, 'category':category_obj})

@login_required
def create_content(request, section_id):
    # content_model = get_model(model_name)
    try:
        section = CourseSection.objects.filter(id=section_id).first()

    except CourseSection.MultipleObjectsReturned:
        print("Exception ERROR: multiple objects returned!")

    if request.method == 'POST':
        content_formset = ContentFormSet(
                                instance = section,
                                data=request.POST,
                                files=request.FILES)
        if content_formset.is_valid():
            content_formset.save()
            # section_formset = CourseSectionFormSet(instance=course)
        else:
            messages.error(request, 'error creating the content')

    content_formset = ContentFormSet(instance=section)
    return render(request, 'courses/create_content.html', {'content_formset':content_formset, 'section':section})
@login_required
def edit_content(request, content_id):

    try:
        content = ContentItem.objects.filter(id=content_id)[0]
    except ContentItem.MultipleObjectsReturned:
        print("Exception ERROR: multiple objects returned!")

    if request.method == 'POST':
        edit_content_form = ContentForm(instance=content, data=request.POST, files=request.FILES)
        if edit_content_form.is_valid():
            edit_content_form.save()
        else:
            messages.error(request, 'error updating the content')

    else:
        edit_content_form = ContentForm(instance=content)
    return render(request, 'courses/edit_content.html', {'edit_content_form':edit_content_form ,'content':content})

# def get_model(model_name):
#     if model_name in ['image', 'video', 'file']:
#         return apps.get_model(app_label='courses', model_name=model_name)
#     return None
@login_required
def edit_section(request, section_id):

    try:
        section = CourseSection.objects.filter(id=section_id).first()
    except CourseSection.MultipleObjectsReturned:
        print("Exception ERROR: multiple objects returned!")

    try:
        contents = ContentItem.objects.all().filter(course_section=section)
    except ContentItem.MultipleObjectsReturned:
        print("Exception ERROR: multiple objects returned")

    if request.method == 'POST':
        edit_section_form = CourseSectionForm(instance=section, data=request.POST)
        if edit_section_form.is_valid():
            edit_section_form.save()
        else:
            messages.error(request, 'error updating the section info')

    else:
        edit_section_form = CourseSectionForm(instance=section)
    content_formset = ContentFormSet(instance=section)
    return render(request, 'courses/edit_section.html', {'edit_section_form':edit_section_form, 'section':section, 'contents':contents, 'content_formset':content_formset})

def get_content_formsets(instance):

        formset = ContentFormSet(instance=instance)

        return formset

# def get_content_formset(content_type, instance, data, files):
#     if content_type=='video':
#         formset = VideoContentFormSet(instance=instance, data=data, files=files)
#         return formset
#
#     if content_type=='image':
#         formset = ImageContentFormSet(instance=instance, data=data, files=files)
#         return formset
#
#     if content_type=='file':
#         formset = FileContentFormSet(instance=instance, data=data, files=files)
#         return formset


@login_required
def create_section(request, course_id):

    try:
        course = Course.objects.filter(id=course_id).first()
    except Course.MultipleObjectsReturned:
        print("Exception ERROR: multiple objects returned!")

    if request.method == 'POST':
        section_form =  CourseSectionForm(instance=course, data=request.POST, files=request.FILES)
        if section_form.is_valid():
            section = section_form.save()
            # section_formset = CourseSectionFormSet(instance=course)
            return HttpResponseRedirect(reverse("courses:edit_section", args=[section.id]))

        else:
            messages.error(request, 'error creating the course')

    section_form = CourseSectionForm(instance=course)
    return render(request, 'courses/create_section.html', {'section_form':section_form, 'course':course})


@login_required
def edit_course(request, oid):

    try:
        course = Course.objects.filter(id=oid).first()
    except Course.MultipleObjectsReturned:
        print("Exception ERROR: multiple objects returned!")

    try:
        sections = CourseSection.objects.all().filter(course=course)
    except CourseSection.MultipleObjectsReturned:
        print("Exception ERROR: multiple objects returned")
    net_sections = []
    for section in sections:
        if section.section_name != "":
            net_sections.append(section)

    if request.method == 'POST':
        edit_course_form = CourseInfoForm(instance=course, data=request.POST, files=request.FILES)
        if edit_course_form.is_valid():
            edit_course_form.save()
        else:
            messages.error(request, 'error updating the course')
    else:
        edit_course_form = CourseInfoForm(instance=course)
    return render(request, 'courses/edit_course.html', {'edit_course_form':edit_course_form, 'course':course, 'sections':net_sections})

@login_required
def list_courses(request):
    profile=request.user.profile
    course_list = InstructorCoursesList.objects.filter(profile=profile).first()

    try:
        courses = Course.objects.all().filter(instructor_course_list=course_list)
    except Course.MultipleObjectsReturned:
        print("Exception ERROR: multiple objects returned")
    return render(request, 'courses/courses_list.html', {'courses':courses})

@login_required
def create_course(request):
    profile=request.user.profile
    # profile = Profile(user=request.user)
    course_list = InstructorCoursesList.objects.filter(profile=profile).first()
    # Must save it first before assign it
    # course_list.save()
    course = Course(instructor_course_list=course_list)
    # section_formset = CourseSectionFormSet(instance=course)

    if request.method == 'POST':
        new_course_form = CourseInfoForm(instance=course, data=request.POST, files=request.FILES)
        if new_course_form.is_valid():
            new_course_form.save()
            print("Created course..")
            #works without the args also
            return HttpResponseRedirect(reverse("courses:edit_course", args=[course.id]))

        else:
            messages.error(request, 'error creating the course')
    else:
        print("here...")
        new_course_form = CourseInfoForm()
    return render(request, 'courses/create_course.html', {'new_course_form':new_course_form})
