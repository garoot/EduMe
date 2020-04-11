from django.contrib import admin
from .models import Blog, BlogComment, BlogSection, Category

# Register your models here.
admin.site.register(Blog)
admin.site.register(BlogSection)
admin.site.register(BlogComment)
admin.site.register(Category)
