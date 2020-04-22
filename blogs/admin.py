from django.contrib import admin
from .models import Blog, BlogComment, BlogSection, Category

admin.site.register(BlogSection)
admin.site.register(BlogComment)
admin.site.register(Category)


class BlogSectionInline(admin.StackedInline):
    model = BlogSection

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    inlines = [BlogSectionInline]
# Register your models here.
# admin.site.register(Blog)
# admin.site.register(BlogSection)
# admin.site.register(BlogComment)
# admin.site.register(Category)
