from django import forms
# from django.contrib.auth.models import User
from .models import Course, CourseSection, CourseReport, Video, File, OrderItem, Order, Image, Category, Subcategory

class CourseInfoForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['course_name', 'course_topic', 'course_price'
            , 'course_title', 'course_outline', 'course_requirements'
            , 'course_outcomes', 'course_description', 'target_students'
            , 'course_picture', 'course_category', 'course_subcategory'
                ]
        # widgets = {
        #     'course_name': forms.TextInput( attrs={'required': True}),
        #      'course_topic': forms.TextInput( attrs={'required': True}),
        #      'course_price': forms.FloatField(),
        #      'course_title': forms.TextInput( attrs={'required': True} ),
        #      'course_outline': forms.TextInput( attrs={'required': True} ),
        #      'course_level': forms.TextInput( attrs={'required': True}),
        #      'course_requirements': forms.TextInput( attrs={'required': True} ),
        #      'course_outcomes': forms.TextInput( attrs={'required': True} ),
        #      'course_description': forms.TextInput( attrs={'required': True} ),
        #      'target_students': forms.TextInput( attrs={'required': True} ),
        #      'course_category': forms.TextInput( attrs={'required': True} ),
        #      'course_subcategory': forms.TextInput( attrs={'required': True} ),
        #      }

class CourseSectionForm(forms.ModelForm):
    class Meta:
        model = CourseSection
        fields = ['section_num', 'section_name']
        # widgets = {
        #     'section_num': forms.IntegerField( attrs={'required': True}),
        #     'section_name': forms.TextInput( attrs={'required': True}),
        # }
