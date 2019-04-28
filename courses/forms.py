from django import forms
# from django.contrib.auth.models import User
from .models import Course, CourseSection, CourseReport, Video, File, OrderItem, Order, Image, Category, Subcategory

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['course_name', 'course_topic', 'course_price'
            , 'course_title', 'course_outline', 'course_requirement'
            , 'course_outcomes', 'course_description', 'target_students'
            , 'course_picture', 'course_category', 'course_subcategory'
                ]
        widgets = {
            'course_name': forms.TextInput(required=True, attrs={'placeholder': }),
             'course_topic': forms.TextInput(required=True, attrs={'placeholder': }),
             'course_price': forms.TextInput(attrs={'placeholder': },
             'course_title': forms.TextInput(required=True, attrs={'placeholder': }),
             'course_outline': forms.TextInput(required=True, attrs={'placeholder': }),
             'course_level': forms.TextInput(required=True)
             'course_requirement': forms.TextInput(required=True, attrs={'placeholder': }),
             'course_outcomes': forms.TextInput(required=True, attrs={'placeholder': }),
             'course_description': forms.TextInput(required=True, attrs={'placeholder': }),
             'target_students': forms.TextInput(required=True, attrs={'placeholder': }),
             'course_picture': forms.TextInput(attrs={'placeholder': }),
             'course_category': forms.TextInput(required=True, attrs={'placeholder': }),
             'course_subcategory': forms.TextInput(required=True, attrs={'placeholder': }),
             }

class CourseSectionForm(forms.ModelForm):
    class Meta:
        model = CourseSection
        fields = ['section_num', 'section_name']
        widgets = {
            'section_num': forms.int(required=True),
            'section_name': forms.TextInput
        }
