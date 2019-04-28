from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    url(r'^login/$', views.user_login, name = 'login'),
    url(r'^register/$', views.register, name = 'register'),
    url(r'^instructor_application/$', views.instructor_application, name = 'instructor_application'),
    url(r'^dashboard/$', views.dashboard, name = 'dashboard'),
    url(r'^logout/$', views.user_logout, name = 'logout'),
    url(r'^editProfile$', views.edit_profile, name='edit_profile'),
    url(r'^view_applications$', views.list_applications, name='list_applications'),
    url(r'^display_application/(?P<oid>[0-9]+)/$', views.display_application, name='display_application'),
    url(r'^process_application/(?P<approved>[01])/(?P<oid>[0-9]+)/$', views.process_application, name='finish_application'),
]
