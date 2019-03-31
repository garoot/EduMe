from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url('InstructorRegistration/', views.instructor_registration, name='instructor_registration'),

]
