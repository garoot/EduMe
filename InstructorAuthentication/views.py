from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from InstructorAuthentication.forms import NewInstructorForm
from InstructorAuthentication.models import Instructor, InstructorCourses
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request, 'EduMe/index.html')

def instructor_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse(index))

#to handle the registration process
def instructor_login(request):

    if request.method == 'POST':
        instructor = instructor()

        emailAddress = request.post.get('instructor_username')
        instructorPassword = request.post.get('instructor_password')

        instructor = authenticate(username=emailAddress, password=instructorPassword)

        if instructor:
            if instructor.is_active:
                login(request, instructor)
                return HttpResponseRedirect(reverse(instructor_page))
            else:
                return HttpResponse('Account not active')

        return HttpResponse('Login Failed!')

    else:
        return render(request, 'InstructorAuthentication/InstructorLandingPage.html', {'instructor': instructor})


def instructor_registration(request):

    form = NewInstructorForm()
    if 'EmailAddress' in request.POST:
        print("Hello World")
        form = NewInstructorForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponse('InstructorAuthentication/InstructorRegistration.html',{'form':form})


            # return render(request, 'EduMe/index.html',
            #                  {'form': form})
        else:
            # messages.error(request, "Error")
            return HttpResponse('EduMe/index.html',{'form':form})

    else:
        return render(request, 'InstructorAuthentication/InstructorRegistration.html', {'form':form})
