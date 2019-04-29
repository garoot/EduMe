from django.contrib import admin
from .models import Course, CourseSection, CourseReport, Video, File, OrderItem, Order, Image, Category, Subcategory

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    pass

class SubcategoryAdmin(admin.ModelAdmin):
    pass

class CourseAdmin(admin.ModelAdmin):
    list_display = ['course_name', 'course_description', 'created', 'course_picture']

admin.site.register(Category,CategoryAdmin)
admin.site.register(Subcategory, SubcategoryAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(CourseSection)
admin.site.register(CourseReport)
admin.site.register(Video)
admin.site.register(File)
admin.site.register(Image)
admin.site.register(OrderItem)
admin.site.register(Order)
