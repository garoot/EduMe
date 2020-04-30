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
class BlogDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BlogDetailSerializer
    queryset = Blog.objects.all()

# USED IT BEFORE TO INCLUDE IT IN ONE ADMIN CONTROL PAGE (Blogs)
    # class BlogSectionListlView(generics.ListCreateAPIView):
    #     queryset = BlogSection.objects.all()
    #     serializer_class = BlogSectionDetailSerializer

# USED IT BEFORE TO INCLUDE IT IN ONE ADMIN CONTROL PAGE (Blogs)
    # class BlogSectionDetailView(generics.RetrieveUpdateDestroyAPIView):
    #     queryset = BlogSection.objects.all()
    #     serializer_class = BlogSectionDetailSerializer

class BlogCommentListView(generics.ListCreateAPIView):
    queryset = BlogComment.objects.all()
    serializer_class = BlogCommentsSerializer




