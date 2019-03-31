from django.shortcuts import render
from InstructorAuthentication.forms import NewInstructorForm
from InstructorAuthentication.models import Instructor, InstructorCourses

# Create your views here.

def index(request):
    return render(request, 'EduMe/index.html')

#to handle the registration process
def instructor_registration(request):

    form = NewInstructorForm()

    if request.method == "POST":
        form = NewInstructorForm(request.POST)

        if form.is_valid():
            form.save(commit=TRUE)

            return render(request, 'EduMe/index.html',
                            {})
        else:
            print("Error!")

    else:
        return render(request, 'InstructorAuthentication/InstructorRegistration.html',
                        {'form': form})
