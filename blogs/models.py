from django.db import models
from django.utils import timezone
from accounts.models import Profile, BloggerBlogList
from courses.models import Category
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User



CATEGORIES =(
    ('0', 'Science'),
    ('1', 'Math & Algebra'),
    ('2', 'Development Tutorials'),
    ('3', 'Tech-Related'),
    ('none', 'None'),
    )
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255, default="", unique=True)

    def __str__(self):
        return self.name

class Blog(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, related_name='blogs')  
    # author = models.ForeignKey(
    #     User, on_delete=models.SET_NULL, null=True, related_name='blogs')
    blogger_bloglist = models.ForeignKey(BloggerBlogList, on_delete=models.SET_NULL, related_name="blogs", blank=False, null=True)
    blog_title = models.CharField(max_length=255)
    blog_description = models.TextField(max_length=255, blank=True, null=True)   
    publish_date = models.DateTimeField(default=timezone.now, editable=False)
    blog_picture = models.ImageField(upload_to='blogs/%Y/%m/%d', blank=True, null=True)
    blog_category = models.ForeignKey(Category, on_delete=models.PROTECT)
    content = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.blog_title

    # def full_name(self):
    #     return (self.author.full_name())


# class BlogSection(models.Model):
#     blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="sections")
#     section_topic = models.CharField(max_length=255)
#     content = RichTextField(blank=True, null=True)

#     def __str__(self):
#         return self.section_topic

class BlogComment(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="comments")
    text = models.TextField(max_length=355)

