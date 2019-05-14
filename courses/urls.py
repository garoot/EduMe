from django.conf.urls import url, include
from django.urls import path
from . import views

app_name='courses'

urlpatterns = [
    url(r'^create_course/$', views.create_course, name='create_course'),
    url(r'^list_courses/$', views.list_courses, name='list_courses'),
    url(r'^edit_course/(?P<oid>[0-9]+)/$', views.edit_course, name='edit_course'),
    url(r'^create_section/(?P<course_id>[0-9]+)/$', views.create_section, name='create_section'),
    url(r'^edit_section/(?P<section_id>[0-9]+)/$', views.edit_section, name='edit_section'),
    url(r'^create_content/(?P<section_id>[0-9]+)/$', views.create_content, name='create_content'),
    url(r'^edit_content/(?P<content_id>[0-9]+)/$', views.edit_content, name='edit_content'),


]
