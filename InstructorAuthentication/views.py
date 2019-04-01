from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from InstructorAuthentication.forms import NewInstructorForm
from InstructorAuthentication.models import Instructor, InstructorCourses

# Create your views here.

def index(request):
    return render(request, 'EduMe/index.html')

#to handle the registration process
def instructor_registration(request):

    form = NewInstructorForm()

    if 'EmailAddress' in request.POST:
        print("Hello World")
        form = NewInstructorForm(request.POST)

        if form.is_valid():
            print("here")
            form.save()
            return HttpResponse('InstructorAuthentication/InstructorRegistration.html',{'form':form})


            # return render(request, 'EduMe/index.html',
            #                  {'form': form})
        else:
            # messages.error(request, "Error")
            return HttpResponse('EduMe/index.html',{'form':form})

    else:
        return render(request, 'InstructorAuthentication/InstructorRegistration.html',
                        {'form': form})
