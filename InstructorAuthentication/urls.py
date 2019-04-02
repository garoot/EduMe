from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path
from . import views

app_name = 'InstructorAuthentication'

urlpatterns = [
    # path('admin/', admin.site.urls),
    url(r'^$', views.instructor_login, name='instructor_page'),
    url('InstructorRegistration/', views.instructor_registration, name='new_instructor'),
    # url('InstructorLogin/', views.instructor_login, name='instructor_login'),

]
