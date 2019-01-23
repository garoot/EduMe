from django.conf.urls import url
from EduControl import views

urlpatterns = [
    url(r'^$', views.broadcast_station, name='broadcast_station'),
]
