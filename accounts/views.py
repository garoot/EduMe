from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, UserRegistrationForm, InstructorApplicationForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import InstructorApplication, Profile
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()


def index(request):
    return render(request, 'index.html')

    """
    the function list_applications():
    - lists all applications with 'submitted' status
    - get the application's user instance
    - approve/disapprove it and save it
    """
@login_required
def list_applications(request):
    try:
        applications = InstructorApplication.objects.all().filter(status="submitted")
    except InstructorApplication.MultipleObjectsReturned:
        print("Exception ERROR: multiple objects returned!")

    return render(request, 'accounts/applications_list.html', {'applications':applications})

    """
    display_application() displays information of clicked application by:
    - retrieving the application instance and render it to template
    - then display the application's fields (using logics within the template)
    """
@login_required
def display_application(request, oid):
    try:
        application = InstructorApplication.objects.filter(id=oid)[0]
    except InstructorApplication.MultipleObjectsReturned:
        print("Exception ERROR: multiple objects returned!")
    return render(request, 'accounts/application_process.html', {'application':application})

"""
 process_application() takes the command of approval or disapproval given by admins
 and based on that:
 - the applicant's is_instructor field will be True or False.
 - the application status will be 'approved', or rejected.
 - the applicant will no longer see the application option on their dashboard if
    applicant is approved.
"""
@login_required
def process_application(request, approved, oid):

    try:
        application = InstructorApplication.objects.filter(id=oid)[0]
        instructor_profile=application.profile
        if approved:
            print("in the approved if..")
            application.status = 'processed'
            instructor_profile.is_instructor = True
            application.save()
            instructor_profile.save()
        else:
            application.status = 'processed'


    except InstructorApplication.MultipleObjectsReturned:
        print("Exception ERROR: multiple objects returned!")

    """
    if approved:
        - change is_instructor to True
        - change application status to processed
    """
    # Better to return list_applications above :)
    try:
        applications=InstructorApplication.objects.all().filter(status='submitted')
    except InstructorApplication.MultipleObjectsReturned:
        print("Exception ERROR: multiple objects returned!")

    return render(request, 'accounts/applications_list.html', {'applications':applications})

@login_required
def edit_profile(request):
    current_profile = request.user.profile
    if request.method == 'POST':
        profile_form = ProfileUpdateForm(instance=current_profile, data=request.POST, files=request.FILES)
        if profile_form.is_valid():
            profile_form.save()
        else:
            print("form is invalid")
    else:
        profile_form = ProfileUpdateForm(instance=request.user.profile)
    return render(request, 'accounts/edit_profile.html', {'form': profile_form})

@login_required
def instructor_application(request):
    instructor_profile = request.user.profile
    if request.method == 'POST':
        """
        Every user after logging in can submit an application to become an instructor infinite number of times.
        To do this, we will:
        1- create a new instructor application model
        2- link it to the instructor profile
        """
        application = InstructorApplication.objects.create(profile=instructor_profile)
        """
        3- give it as an instance below
        """
        application_form = InstructorApplicationForm(instance=application,data=request.POST)

        if application_form.is_valid():
            application.status = 'submitted'
            application_form.save()
            messages.success(request, 'Successfully submitted')
        else:
            messages.error(request, 'error submitting application')

    else:
        application_form = InstructorApplicationForm()
    return render(request, 'accounts/instructor_application.html', {'form':application_form})

@login_required
def dashboard(request):
    return render(request, 'accounts/dashboard.html')

def register(request):
    if request.method == 'POST':
        register_form = UserRegistrationForm(request.POST)
        if register_form.is_valid():
            # Create a new user but don't save it yet until we hash the password
            new_user = register_form.save(commit=False)
            # Hashing the password
            new_user.set_password(register_form.cleaned_data['password'])
            new_user.save()

            return redirect('accounts:login')

    else:
        register_form = UserRegistrationForm()

    return render(request, 'accounts/register.html', {'form':register_form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            temp = form.cleaned_data
            user = authenticate(username=temp['username'], password=temp['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    if 'next' in request.POST:
                        return redirect(request.POST.get('next'))
                    else:
                        return redirect('accounts:dashboard')

                else:
                    return HttpResponse('Disabled Account')

            else:
                return HttpResponse('Invalid Login')
        else:
            form = LoginForm()
            return render(request, 'accounts/login.html', {'form': form})
    else:
        form = LoginForm()
        return render(request, 'accounts/login.html', {'form':form})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
