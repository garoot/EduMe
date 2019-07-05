from django.conf.urls import url
from . import views

app_name='payment'
urlpatterns = [
    url(r'^process/$', views.process_payment, name='process_payment'),
    url(r'^done/$', views.payment_done, name='payment_done'),
    url(r'^canceled/$', views.payment_canceled, name='payment_canceled'),

]
