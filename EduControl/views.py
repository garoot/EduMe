from django.shortcuts import render
from EduControl.forms import UserForm, UserProfileInfoForm

# Create your views here.
def broadcast_station(request):
    return render(request, 'EduControl/broadcast_station.html')

def index(request):
    return render(request, 'EduMe/index.html')

def register(request):
    registered = False
    user_form = UserForm()
    if request.method == "POST":
        form = UserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
            #or you can return a "Successful Registration" page

        else:
            print("There was an error with one one of the fields")

    return render(request, 'EduControl/register.html', {'form':form})
