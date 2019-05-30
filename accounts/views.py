from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, UserRegistrationForm, InstructorResumeForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import InstructorResume, Profile
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404


User = get_user_model()


def index(request):
    return render(request, 'EduMe/index.html')

    """
    the function list_applications():
    - lists all applications with 'submitted' status
    - get the application's user instance
    - approve/disapprove it and save it
    """
@login_required
def list_applications(request):
    try:
        applications = InstructorResume.objects.all().filter(status="submitted")
    except InstructorResume.MultipleObjectsReturned:
        print("Exception ERROR: multiple objects returned! 3")

    return render(request, 'accounts/applications_list.html', {'applications':applications})

    """
    display_application() displays information of clicked application by:
    - retrieving the application instance and render it to template
    - then display the application's fields (using logics within the template)
    """
@login_required
def display_application(request, oid):
    try:
        application = InstructorResume.objects.filter(id=oid).first()
    except InstructorResume.MultipleObjectsReturned:
        print("Exception ERROR: multiple objects returned! 4")
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
        application = get_object_or_404(InstructorResume, pk=oid)
    except InstructorResume.MultipleObjectsReturned:
        print("Exception ERROR: multiple objects returned! 1")

    if approved == '1':
        print("in approved...")
        application.approve()

    elif approved == '0':
        application.reject()
    """
    if approved:
        - change is_instructor to True
        - change application status to processed
    """
    try:
        applications=InstructorResume.objects.filter(status='submitted')
    except InstructorResume.MultipleObjectsReturned:
        print("Exception ERROR: multiple objects returned! 2")

    return render(request, 'accounts/applications_list.html', {'applications':applications})

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
        application = InstructorResume.objects.create(profile=instructor_profile)
        """
        3- give it as an instance below
        """
        application_form = InstructorResumeForm(instance=application,data=request.POST)

        if application_form.is_valid():
            """
            this submit() method will save the form and change
            the profile.instructor_application_status and application.status
            to 'submitted'
            """
            application.submit()
            messages.success(request, 'Successfully submitted')
        else:
            messages.error(request, 'error submitting application')
        return HttpResponseRedirect(reverse("accounts:instructor_application"))

    else:
        application_form = InstructorResumeForm()
    return render(request, 'accounts/instructor_application.html', {'form':application_form})

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
