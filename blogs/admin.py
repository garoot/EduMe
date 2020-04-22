from django.contrib import admin
from .models import Blog, BlogComment, Category

admin.site.register(BlogComment)
admin.site.register(Category)
admin.site.register(Blog)


# HOW TO INVOLVE TWO MODELS(Blog and BlogSection) INTO ONE CONTROL PAGE (Blog)
# admin.site.register(BlogSection)
# class BlogSectionInline(admin.StackedInline):
#     model = BlogSection
#     extra = 1
# @admin.register(Blog)
# class BlogAdmin(admin.ModelAdmin):
#     inlines = [BlogSectionInline]


