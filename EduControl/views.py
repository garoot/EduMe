from django.shortcuts import render
from EduControl.forms import UserForm, UserProfileInfoForm
from django.http import HttpResponse
# Create your views here.
def broadcast_station(request):
    return render(request, 'EduControl/broadcast_station.html')

def index(request):
    return render(request, 'EduMe/index.html')

def register(request):

    registered = False

    user_form = UserForm()
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            return render(request, 'EduMe/index.html')

            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=True)
            profile.user = user
            profile.save()

        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

        return render(request, 'EduControl/channel_register.html',
        {'user_form':user_form, 'profile_form':profile_form,
        'registered':registered})
