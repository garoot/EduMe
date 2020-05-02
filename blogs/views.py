from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import *


# Create your views here.

# list and create blogs
class BlogListView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogDetailSerializer
class BlogCommentsView(generics.ListCreateAPIView):
    serializer_class = BlogCommentsSerializer

    def get_queryset(self, blog_id):
        #storing Category.id in category
        blog_id = None
        blog_id = self.kwargs['blog_id']
        blog = Blog.objects.get(pk=blog_id)
        #filtering objects related to Category.id
        if blog:
            return BlogComment.objects.filter(blog=blog)  

class CategoryBlogListView(generics.ListCreateAPIView):
    serializer_class = BlogSerializer

    def get_queryset(self):
        #storing Category.id in category
        category = None
        category = self.kwargs['category']
        #filtering objects related to Category.id
        if category:
            return Blog.objects.filter(blog_category=category)

# retreive, update, delete blog
# URL because it passes the pk through URL
class BlogDetailURLView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BlogDetailSerializer
    queryset = Blog.objects.all()


class BlogCommentListView(generics.ListCreateAPIView):
    # queryset = BlogComment.objects.all()
    serializer_class = BlogCommentsSerializer

    def get_queryset(self):
        #storing Category.id in category
        # blog_id = self.kwargs['blog_id']

        blog_id = self.request.query_params.get('blog_id')
        blog = Blog.objects.get(pk=blog_id)
        queryset = BlogComment.objects.filter(blog__id=blog_id)
        # if blog_id is not None:
        #     blog = Blog.objects.get(pk=blog_id)
        #filtering objects related to Category.id
        if blog:
            queryset = queryset.filter(blog__id=blog.id)
        return queryset

class NewsletterListView(generics.ListCreateAPIView):
    queryset = NewsletterEmail.objects.all()
    serializer_class = NewsletterEmailSerializer

    # def create(self, request, *args, **kwargs):

    #     response = 'Already Subscribed *_*'
    #     user_email = self.request.query_params.get('email')

    #     emails = NewsletterEmail.objects.all()
    #     if user_email not in emails:

    #         new_subscriber = NewsletterEmail.objects.create(email=user_email)
    #         response = 'Successfully Subscribed!'

    #         return response

    #     return response 

    
class NewletterEmailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NewsletterEmailSerializer
    queryset = NewsletterEmail.objects.all()




