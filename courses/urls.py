from django.conf.urls import url, include
from django.urls import path
from . import views

app_name='courses'

urlpatterns = [
    url(r'^create_course/$', views.create_course, name='create_course'),
    url(r'^list_courses/$', views.list_courses, name='list_courses'),
    url(r'^edit_course/(?P<oid>[0-9]+)/$', views.edit_course, name='edit_course'),
    url(r'^create_section/(?P<oid>[0-9]+)/$', views.create_section, name='create_section'),


]
