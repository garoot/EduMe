from django import forms
from .models import  InstructorProfile, StudentProfile
from django.contrib.auth import get_user_model, authenticate

User = get_user_model()
class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['first_name','last_name','username', 'email', 'password', 'is_instructor', 'is_student', 'is_promoter']
        widgets = {'password': forms.PasswordInput(),}


class InstructorProfileForm(forms.ModelForm):
    class Meta:
        model = InstructorProfile
        fields = ['country','city','degree','major']

class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = []

class UserLoginForm(forms.ModelForm):
    # username = forms.CharField()
    # password = forms.ChoiceField(widget = forms.PasswordInput())

    class Meta:

        model = User
        fields = ['username', 'password']

    def clean(self, *args, **kwargs):
        # self.cleaned_data = super(UserLoginForm, self).clean(*args,**kwargs)
        data = self.cleaned_data
        username = data.get('username')
        password = data.get('password')
        for field,content in data.items():
            print("{} : {}".format(username, password))
        if username and password:
            print("authenticating within form...")
            user = authenticate(username=username, password=password)
            print ("User: {}, username: {}, password: {}".format(user, username, password))
            if not user:
                raise forms.ValidationError("User does not exist")

            if not user.check_password(password):
                raise forms.ValidationError("Password is incorrect")
                print("password incorrect")

            if not user.is_active:
                raise forms.ValidationError("User is not active")
            else:
                print("data username: {}, data password: {}".format(data.get('username'), data.get('password')))
                for key, content in data.items():
                    print("{}:{}".format(key, content))
        return data
