from django.shortcuts import render
from search.documents import CourseDocument
from courses.models import Category, Subcategory


# Create your views here.
def search_course(request):
    q = request.GET.get('q')
    if q:
        courses = CourseDocument.search().query("match", course_title=q)
        
    else:
        courses = ''

    try:
        categories = Category.objects.all()
    except Category.MultipleObjectsReturned:
        print("Exception ERROR: multiple objects returned!")

    try:
        subcategories = Subcategory.objects.all()
    except Subcategory.MultipleObjectsReturned:
        print("Exception ERROR: multiple objects returned!")

    return render(request, 'courses/shop/catalog.html', {'courses':courses, 'categories':categories, 'subcategories':subcategories, 'category':None})

def search(request):
    return render(request, 'search/search.html')
