from django.forms import ModelForm
from .models import Instructor
from django import forms

class NewInstructorForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta():
        model = Instructor
        exclude = ('UserStatus', 'InstructorStatus','last_login')
