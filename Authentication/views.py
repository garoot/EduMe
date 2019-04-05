from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from Authentication.forms import UserForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from Authentication.models import Instructor, InstructorCourses
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import UserLoginForm

# Create your views here.

def index(request):
    return render(request, 'EduMe/index.html')

@login_required
def instructor_page(request):
    return render(request, 'Instructor/InstructorPage.html')

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST or None)
        print("validating..")

        if form.is_valid():
            print("valid...")
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            print("They used username: {} and password: {}".format(username,password))
            print("Authenticating..")
            user = authenticate(request, username=username, password=password)

            if user is not None:
                print("authenticated...")
                if user.is_active:
                    print("user is active...")
                    login(request, user)
                    return HttpResponseRedirect(reverse('index'))

                else:
                    return HttpResponse("Your Account Isn't Active!!!!")

            else:
                print("Someone tried to login and failed.")
                print("Theyyy used username: {} and password: {}".format(username,password))
                return HttpResponse("Invalid login details given")
        else:
            return HttpResponse("form is not valid")

    else:
        print("not passed first if..")
        form = UserLoginForm()
        return render(request, 'Registration/RegistrationPage.html', {'form':form})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def user_registration(request):

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid:
            user = user_form.save(commit=False)
            user.set_password(user.password)
            user.username = user.username
            print("Reg Username: {}".format(user.username))
            user.save()
            return HttpResponse('EduMe/index.html',{'form':user})
    else:
        user_form = UserForm()
        return render(request, 'Registration/RegistrationPage.html', {'form':user_form})
