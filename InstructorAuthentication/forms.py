from django.forms import ModelForm
from .models import Instructor
from django import forms

class NewInstructorForm(ModelForm):
    # password = forms.CharField(widget=forms.PasswordInput)
    # InstructorEmail = forms.EmailField(required=True)
    BirthDate = forms.DateField(
    widget=forms.widgets.DateInput(format="%m/%d/%Y"))
    class Meta():
        model = Instructor
        exclude = ('UserStatus', 'InstructorStatus','last_login')
        widgets = {
        'password': forms.PasswordInput(),
        }
