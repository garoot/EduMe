from django.conf.urls import url
from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

app_name='blogs'

urlpatterns = [
    # list, create blogs
    path('blogs/', BlogListView.as_view() ),
    path('blogs/<category>/', CategoryBlogListView.as_view()),

    # retrieve, update, destroy blogs
    path('blog/<int:pk>/', BlogDetailURLView.as_view()),
    path('blogcomments/', BlogCommentListView.as_view()),
    path('newsletter/', NewsletterListView.as_view()),

]
