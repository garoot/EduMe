from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import LoginForm, UserRegistrationForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile
from django.urls import reverse
from django.contrib.auth import get_user_model, login, authenticate, logout
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


# @login_required
# def list_applications(request):
#     try:
#         applications = InstructorResume.objects.all().filter(status="submitted")
#     except InstructorResume.MultipleObjectsReturned:
#         print("Exception ERROR: multiple objects returned! 3")

#     return render(request, 'accounts/applications_list.html', {'applications': applications})

#     """
#     display_application() displays information of clicked application by:
#     - retrieving the application instance and render it to template
#     - then display the application's fields (using logics within the template)
#     """


# @login_required
# def display_application(request, oid):
#     try:
#         application = InstructorResume.objects.filter(id=oid).first()
#     except InstructorResume.MultipleObjectsReturned:
#         print("Exception ERROR: multiple objects returned! 4")
#     return render(request, 'accounts/application_process.html', {'application': application})


"""
 process_application() takes the command of approval or disapproval given by admins
 and based on that:
 - the applicant's is_instructor field will be True or False.
 - the application status will be 'approved', or rejected.
 - the applicant will no longer see the application option on their dashboard if
    applicant is approved.
"""
# @login_required
# def process_application(request, approved, oid):
#     try:
#         application = InstructorResume.objects.get(pk=oid)
#     except InstructorResume.MultipleObjectsReturned:
#         print("Exception ERROR: multiple objects returned! 1")

#     if approved == '1':
#         print("in approved...")
#         application.approve()

#     elif approved == '0':
#         application.reject()
#     """
#     if approved:
#         - change is_instructor to True
#         - change application status to processed
#     """
#     try:
#         applications = InstructorResume.objects.filter(status='submitted')
#     except InstructorResume.MultipleObjectsReturned:
#         print("Exception ERROR: multiple objects returned! 2")

#     return render(request, 'accounts/applications_list.html', {'applications': applications})


# @login_required
# def instructor_application(request, application_form=None, oid=None):
#     instructor_profile = request.user.profile
#     if request.method == 'POST':
#         """
#         Every user after logging in can submit an application to become an instructor infinite number of times.
#         To do this, we will:
#         1- create a new instructor application model
#         2- link it to the instructor profile
#         """

#         if (application_form != None) and (oid != None):
#             try:
#                 application = InstructorResume.objects.get(pk=oid)
#             except InstructorResume.MultipleObjectsReturned:
#                 print("Exception ERROR: multiple objects returned! 1")
#             """
#             no need to redefine application_form here since it's passed as argument
#             """
#             application_form = application_form
#             # application_form = InstructorResumeForm(instance=application,data=request.POST)

#         else:
#             application = InstructorResume.objects.create(
#                 profile=instructor_profile)
#             application_form = InstructorResumeForm(
#                 instance=application, data=request.POST)
#         """
#         3- give it as an instance below
#         """
#         if application_form.is_valid():
#             """
#             this submit() method will save the form and change
#             the profile.instructor_application_status and application.status
#             to 'submitted'
#             """
#             print("application_form is valid...being submitted")
#             application.submit()
#         #     messages.success(request, 'Successfully submitted')
#         else:
#             messages.error(request, 'error submitting application')

#         return HttpResponseRedirect(reverse("accounts:instructor_application"))
#     else:
#         application_form = InstructorResumeForm()

#     return render(request, 'accounts/instructor_application.html', {'form': application_form})


@login_required
def edit_profile(request):
    current_profile = request.user.profile
    if request.method == 'POST':
        profile_form = ProfileUpdateForm(
            instance=current_profile, data=request.POST, files=request.FILES)
        if profile_form.is_valid():
            profile_form.save()
        else:
            print("form is invalid")
    else:
        profile_form = ProfileUpdateForm(instance=current_profile)
    return render(request, 'accounts/edit_profile.html', {'form': profile_form})


@login_required
def dashboard(request):
    return render(request, 'accounts/dashboard.html')

def register(request, registration_form=None):
    if request.method == 'POST':

        if registration_form == None:
            registration_form = UserRegistrationForm(request.POST)
        else:
            registration_form = registration_form

        if registration_form.is_valid():
            # Create a new user but don't save it yet until we hash the password
            new_user = registration_form.save(commit=False)
            # Hashing the password
            new_user.set_password(registration_form.cleaned_data['password'])
            new_user.save()
            # Profile.objects.get_or_create(user=request.user)

        messages.error(request, 'error submitting application')
        return HttpResponseRedirect(reverse('accounts:login'))

    else:
        registration_form = UserRegistrationForm()

    return render(request, 'accounts/register.html', {'form': registration_form})


def user_login(request, login_form=None):
    if request.method == 'POST':
        if login_form == None:
            login_form = LoginForm(request.POST)
        else:
            login_form = login_form
        if login_form.is_valid():
            temp = login_form.cleaned_data
            user = authenticate(
                username=temp['username'], password=temp['password'])
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
            login_form = LoginForm()
            return render(request, 'accounts/login.html', {'form': login_form})
    else:
        login_form = LoginForm()
        return render(request, 'accounts/login.html', {'form': login_form})


@login_required
def user_logout(request, client=None):
    if client != None:
        logout(client)
    else:
        logout(request)
    return redirect('accounts:login')
