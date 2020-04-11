from django.db import models
from django.utils import timezone
from accounts.models import Profile, BloggerBlogList
from courses.models import Category


CATEGORIES =(
    ('0', 'Science'),
    ('1', 'Math & Algebra'),
    ('2', 'Development'),
    ('none', 'None'),
    )
# Create your models here.
class Blog(models.Model):
    # author = models.ForeignKey(Profile, on_delete=models.SET_NULL, related_name='blogs')  
    blogger_bloglist = models.ForeignKey(BloggerBlogList, on_delete=models.SET_NULL, related_name="blogs", null=True)
    blog_title = models.CharField(max_length=255)
    blog_description = models.TextField(max_length=255, blank=True, null=True)   
    publish_date = models.DateTimeField(default=timezone.now, editable=False)
    blog_picture = models.ImageField(upload_to='blogs/%Y/%m/%d', blank=True, null=True)
    blog_category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name="blogs", blank=True, null=True)

    def __str__(self):
        return self.blog_title

class BlogSection(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="sections")
    section_topic = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.section_topic

class BlogComment(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="comments")
    text = models.TextField(max_length=355)

