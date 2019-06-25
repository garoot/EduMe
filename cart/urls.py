from django.conf.urls import url, include
from django.urls import path
from . import views

app_name='cart'

urlpatterns = [

    url(r'^cart_add/(?P<course_id>\d+)/$', views.cart_add, name='cart_add'),
    url(r'^cart_detail/$', views.cart_detail, name='cart_detail'),
    url(r'^cart_remove/(?P<course_id>\d+)/$', views.cart_remove, name='cart_remove'),


]
