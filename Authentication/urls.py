from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path
from . import views

app_name = 'Authentication'

urlpatterns = [
    #later change the path to include Instructor App where all updating of instructor info occurs
    url(r'InstructorPage', views.instructor_page, name='instructor_page'),
    url(r'InstructorPage', views.user_logout, name='user_logout'),

    url(r'^$', views.user_registration, name='new_user'),
    url('UserLogin/', views.user_login, name='login'),

]
