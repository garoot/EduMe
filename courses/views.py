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
        course = Course.objects.get(pk=course_id)
    except Course.MultipleObjectsReturned:
        print("Exception ERROR: multiple objects returned!")

    try:
        sections = CourseSection.objects.all().filter(course=course)
    except CourseSection.MultipleObjectsReturned:
        print("Exception ERROR: multiple objects returned")

    net_contents = []
    for section in sections:
        try:
            contents = ContentItem.objects.all().filter(course_section=section)
        except CourseSection.MultipleObjectsReturned:
            print("Exception ERROR: multiple objects returned")
        for content in contents:
            net_contents.append(content)




    return render(request, 'courses/contents/course_page.html', {'course':course, 'sections':sections, 'contents':net_contents})

def display_catalog(request, category_id=None, subcategory=None, type=None):
    category_obj = None
    print("Category: {}".format(category_id))
    if category_id==None :
        try:
            courses = Course.objects.all()
        except Course.MultipleObjectsReturned:
            print("Exception ERROR: multiple objects returned!")
        subcategory = None

    if category_id:
        print("Passed category condition")

        # try:
        category_obj = Category.objects.get(pk=category_id)
        #     print("Category: {}".format(category_obj.name))
        # except Category.MultipleObjectsReturned:
        #     print("Exception ERROR: multiple objects returned!")

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
def create_content(request, section_id, content_form=None):
    # content_model = get_model(model_name)
    print("create_content: step 1")
    try:
        section = CourseSection.objects.get(pk=section_id)

    except CourseSection.MultipleObjectsReturned:
        print("Exception ERROR: multiple objects returned!")

    print(["got the section id: {}".format(section.id)])

    if request.method == 'POST':
        if content_form == None:
            print("content_form is None")
            content_form = ContentForm(
                                    data=request.POST,
                                    files=request.FILES)
        if content_form.is_valid():
            print("Content_formset is valid")
            saved_content = content_form.save(commit=False)
            saved_content.course_section = section
            saved_content.save()
            print("content id: {}".format(saved_content.id))
            # section_formset = CourseSectionFormSet(instance=course)
            return HttpResponseRedirect(reverse("courses:edit_content", args=[saved_content.id]))

        else:
            messages.error(request, 'error creating the content')

    content_form = ContentForm(instance=section)
    return render(request, 'courses/create_content.html', {'content_form':content_form, 'section':section})

@login_required
def edit_content(request, content_id, edit_content_form=None, test_save=None, test_delete=None):
    try:
        content = ContentItem.objects.get(pk=content_id)
    except ContentItem.MultipleObjectsReturned:
        print("Exception ERROR: multiple objects returned!")

    section_id = content.course_section.id
    section = CourseSection.objects.get(pk=section_id)

    if request.method == 'POST':
        if edit_content_form ==None:
            edit_content_form = ContentForm(instance=content, data=request.POST, files=request.FILES)

        if ('save' in request.POST) or test_save:
            if edit_content_form.is_valid():
                print("it's valid..")
                edited_content = edit_content_form.save()
                edited_content.course_section = section
                edited_content.save()

                return HttpResponseRedirect(reverse("courses:edit_section", args=[section_id]))

        elif ('delete' in request.POST) or test_delete:
            content.delete()
            return HttpResponseRedirect(reverse("courses:edit_section", args=[section_id]))

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
def edit_section(request, section_id, edit_section_form=None, test_save=None, test_delete=None):
    print("section id: {}".format(section_id))
    # try:
        # section = CourseSection.objects.filter(id=section_id).first()
    section = CourseSection.objects.get(pk=section_id)
    # except CourseSection.MultipleObjectsReturned:
    #     print("Exception ERROR: multiple objects returned!")

    course_id = section.course.id
    course= Course.objects.get(pk=course_id)

    try:
        contents = ContentItem.objects.all().filter(course_section=section)
    except ContentItem.MultipleObjectsReturned:
        print("Exception ERROR: multiple objects returned")

    if request.method == 'POST':

        if edit_section_form ==None:
            edit_section_form = CourseSectionForm(instance=section, data=request.POST)

        if ('save' in request.POST) or test_save:
            if edit_section_form.is_valid():
                edit_section_form.save()
                return HttpResponseRedirect(reverse("courses:edit_section", args=[section.id]))

        elif ('delete' in request.POST) or test_delete:
            section.delete()
            return HttpResponseRedirect(reverse("courses:edit_course", args=[course.id]))


        else:
            messages.error(request, 'error updating the section info')

    else:
        edit_section_form = CourseSectionForm(instance=section)
    return render(request, 'courses/edit_section.html', {'edit_section_form':edit_section_form, 'section':section, 'contents':contents})

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
def create_section(request, course_id, section_form=None):
    try:
        course = Course.objects.get(pk=course_id)
    except Course.MultipleObjectsReturned:
        print("Exception ERROR: multiple objects returned!")

    if request.method == 'POST':

        if section_form == None:
            section_form =  CourseSectionForm(data=request.POST, files=request.FILES)

        if section_form.is_valid():
            section = section_form.save(commit=False)
            section.course = course
            section.save()
            print("section id: {}".format(section.id))
            # section_formset = CourseSectionFormSet(instance=course)
            return HttpResponseRedirect(reverse("courses:edit_section", args=[section.id]))

        else:
            messages.error(request, 'error creating the course')

    section_form = CourseSectionForm()
    return render(request, 'courses/create_section.html', {'section_form':section_form, 'course':course})

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
def edit_course(request, oid, edit_course_form=None, test_save=None, test_delete=None):
    try:
        course = Course.objects.get(pk=oid)
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

        if edit_course_form == None:
            edit_course_form = CourseInfoForm(instance=course, data=request.POST, files=request.FILES)

        if ('save' in request.POST) or test_save:
            if edit_course_form.is_valid():
                edit_course_form.save()
                return HttpResponseRedirect(reverse("courses:edit_course", args=[course.id]))

        elif ('delete' in request.POST) or test_delete:
            course.delete()
            next = request.POST.get('next','/')
            return HttpResponseRedirect(reverse('courses:list_courses'))
        else:
            messages.error(request, 'error updating the course')
    else:
        edit_course_form = CourseInfoForm(instance=course)
    return render(request, 'courses/edit_course.html', {'edit_course_form':edit_course_form, 'course':course, 'sections':net_sections})

@login_required
def create_course(request, new_course_form=None):
    profile=request.user.profile
    # profile = Profile(user=request.user)
    course_list = InstructorCoursesList.objects.filter(profile=profile).first()
    # Must save it first before assign it
    # course_list.save()
    # section_formset = CourseSectionFormSet(instance=course)

    if request.method == 'POST':
        course = Course.objects.create(instructor_course_list=course_list)

        if new_course_form==None:
            new_course_form = CourseInfoForm(instance=course, data=request.POST, files=request.FILES)

        if new_course_form.is_valid():
            new_course_form.save()
            print("Created course..")
            #works without the args also
            return HttpResponseRedirect(reverse("courses:edit_course", args=[course.id]))

        else:
            messages.error(request, 'error creating the course')
    else:
        new_course_form = CourseInfoForm()
    return render(request, 'courses/create_course.html', {'new_course_form':new_course_form})
