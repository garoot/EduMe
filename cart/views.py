from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from courses.models import Course
from .cart import Cart
from .forms import CartAddProductForm

@require_POST
def cart_add(request, course_id):
    cart = Cart(request)
    course = get_object_or_404(Course, id=course_id)
    cart.add(course=course,
            update_quantity=True)
    cart.save()
    return redirect('cart:cart_detail')

def cart_remove(request, course_id):
    cart = Cart(request)
    course = get_object_or_404(Course, id=course_id)
    cart.remove(course)
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    # course_ids = cart.get_keys()

    # courses = Course.objects.filter(id__in=course_ids)

    return render(request, 'cart/cart_detail.html', {'cart': cart})
