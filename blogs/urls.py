from django.conf.urls import url
from django.urls import path
from .views import BlogListView, BlogDetailView
from django.conf.urls.static import static
from django.conf import settings

app_name='blogs'

urlpatterns = [
    path('blogs/', BlogListView.as_view() ),
    path('blog/<int:pk>/', BlogDetailView.as_view())
]
