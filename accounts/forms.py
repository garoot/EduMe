from django import forms
from django.contrib.auth.models import User
from .models import Profile, InstructorResume

class LoginForm(forms.Form):
   username = forms.CharField()
   password = forms.CharField(widget=forms.PasswordInput)

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
         model = User
         fields = ['username', 'first_name', 'last_name', 'email']

    def clean_password2(self):
        temp = self.cleaned_data
        if temp['password'] != temp['password2']:
            raise forms.ValidationError('Password don\'t match.')
        return temp['password2']
class ApproveApplicationForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['is_instructor']
        widgets = {
        'is_instructor': forms.BooleanField(required=True)
        }
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['country', 'city', 'nationality','dob', 'photo']
        widgets = {
        'dob': forms.DateInput(format='%m/%d/%Y', attrs={'placeholder': 'mm/dd/yyyy'}),
        'country': forms.TextInput(attrs={'placeholder': 'Country of Residence'}),
        'city': forms.TextInput(attrs={'placeholder': 'City of Residence'}),
        'nationality': forms.TextInput(attrs={'placeholder': 'Nationality'})
        }
class InstructorResumeForm(forms.ModelForm):
    class Meta:
        model = InstructorResume
        fields = ['degree', 'major', 'experience']
