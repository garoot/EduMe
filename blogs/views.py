from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import *


# Create your views here.

# list and create blogs
class BlogListView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

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

class BlogSectionListlView(generics.ListCreateAPIView):
    queryset = BlogSection.objects.all()
    serializer_class = BlogSectionDetailSerializer


class BlogSectionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogSection.objects.all()
    serializer_class = BlogSectionDetailSerializer




