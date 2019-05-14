from django.contrib import admin
from .models import Course, CourseSection,ContentItem, CourseReport, OrderItem, Order, Category, Subcategory

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
admin.site.register(ContentItem)
admin.site.register(OrderItem)
admin.site.register(Order)
