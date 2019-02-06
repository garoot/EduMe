from django import forms
from django.contrib.auth.models import User
from EduControl.models import UserProfileInfo

class UserForm(forms.ModelForm):

    class Meta():
        model = User
        fields = ('username','first_name','last_name','password', 'email',)
    password = forms.CharField(widget=forms.PasswordInput())

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        # exclude = ('user',)
        exclude = ('username',)
