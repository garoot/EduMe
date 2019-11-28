from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.decorators.http import require_POST
from courses.models import Course, Order, OrderItem
from .cart import Cart
from .forms import CartAddProductForm
from .tasks import order_created
from django.contrib.auth.decorators import login_required
from celery import task

@require_POST
@login_required
def cart_add(request, course_id):
    cart = Cart(request)
    course_ids = cart.items_ids()
    course_id = int(course_id)
    course = get_object_or_404(Course, id=course_id)
    try:
        order_id = request.session['order_id']
    except:
        print("no order_id")
    """
    creating order and order_item
    """
    profile = request.user.profile
    order_id = None

    """
    if course not in the cart, add to the cart
    """

    if course_id not in course_ids:
        cart.add(course=course,
                update_quantity=True)
        cart.save()

        if order_id:
            order = get_object_or_404(Order, id=order_id)
            print("order {} exists".format(order.id))

        else:
            order = Order.objects.create(profile=profile, total_amount=cart.get_total_price())
            request.session['order_id'] = order.id
        order_item = OrderItem.objects.create(order=order, course=course, purchase_price=course.course_price)
        order_item.order = order
        order_item.save()
        order.total_amount = float(cart.get_total_price())
        order.save()
    else:
        print("item already in cart..")

    print("order total amount: {}".format(order.total_amount))
    cart.print_items()
    return redirect('cart:cart_detail')

def cart_remove(request, course_id):
    cart = Cart(request)
    course_id = int(course_id)
    order_id = request.session['order_id']
    order = get_object_or_404(Order, id=order_id)
    order_items = OrderItem.objects.all().filter(order=order)
    course = get_object_or_404(Course, id=course_id)
    for item in order_items:
        if course_id == item.course.id:
            print("deleting order item..{}".format(course.course_name))
            OrderItem.objects.filter(course=course).delete()
    order.save()
    cart.remove(course)
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    # course_ids = cart.get_keys()

    # courses = Course.objects.filter(id__in=course_ids)

    return render(request, 'cart/cart_detail.html', {'cart': cart})

"""
This function will be modified later to implement the promotion code feature, following these steps:
1. create model with attributes PromotionCode(code, discount_percentage), with code as pk
2. move creating Order and OrderItem from create_order to cart_add() so they are initialized there and can easily update purchase_price
3. add the following lines to cart_add():
    cart = Cart(request)
    profile = request.user.profile
    order_id = request.session['order_id']
    if order_id:
        order = get_object_or_404(Order, id = order_id)
    else:
        order = Order.objects.create(profile=profile, total_amount=cart.get_total_price())
        request.session['order_id'] = order.id
    order_item = OrderItem.objects.create(order=order, course=course, purchase_price=course.course_price)
4. create function apply_promo_code(request, promo_code) in cart/views.py
6. add the following lines to apply_promo_code():
    cart = Cart(request)
    course_ids = self.cart.keys()
    courses = Course.objects.filter(id__in=course_ids)
    profile = request.user.profile
    order_id = request.session['order_id']
    if order_id:
        order = get_object_or_404(Order, id = order_id)
    else:
        print("order has not been created in cart.view.cart_add()")
    order_items = order.items
    for item in order_items:
        course = get_object_or_404(Course, id=item.course.id)
        promo_codes = course.promo_codes
        try:
            promo_code = PromotionCode.objects.filter(code=promo_code)
        except PromotionCode.MultipleObjectsReturned:
            print("Exception ERROR: multiple objects returned! in apply_promo_code()")

        if a course is discounted by admins, promotion codes don't apply

        if (promo_code in promo_codes) && not course.discounted:
            discount_amount = (promo_code.discount_percentage/100) * item.purchase_price
            item.update_purchase_price(discount_amount)
            cart[item.course.id]['price'] = str(item.purchase_price)

7. retrieve order in create_order() using request.session['order_id'] instead of creating new order
8. remove order_item creation from create_order() since it's already created inside order
"""

"""
This is to be removed to order Application
"""
"""
Here, we retrieve order object, which is the receipt and
order.id is basically the receipt number
"""
@login_required
def create_order(request):
    cart = Cart(request)
    course_ids = cart.items_ids()
    print("items ids: {}".format(course_ids))
    courses = Course.objects.filter(id__in=course_ids)
    order_id = request.session['order_id']
    print("order id: {}".format(order_id))
    #will be moved to cart_add
    order = get_object_or_404(Order, id=order_id)
    order_items = OrderItem.objects.all().filter(order=order)

    print(order.total_amount)
    # print(order_items)
    for item in order_items:
        course = item.course
        print("course name: {}".format(course.course_name))
        # course_report = course.report
        # course_report.update_revenue(item.purchase_price)

    cart.clear()
    order_created.delay(order.id)
        #will be moved to cart_add

    return redirect(reverse('payment:process_payment'))

@require_POST
def apply_promo_code(request, code):
    cart = Cart(request)
    course_ids = self.cart.keys()
    courses = Course.objects.filter(id__in=course_ids)
    order_id = request.session['order_id']
    if order_id:
        order = get_object_or_404(Order, id = order_id)
    else:
        print("order has not been created in cart.view.cart_add()")
    order_items = order.items
    for item in order_items:
        course = get_object_or_404(Course, id=item.course.id)
        promo_codes = course.promo_codes
        try:
            promo_code = PromotionCode.objects.get(pk=code)
        except PromotionCode.MultipleObjectsReturned:
            print("Exception ERROR: multiple objects returned! in apply_promo_code()")
        """
        if a course is discounted by admins, promotion codes don't apply
        """
        if (promo_code in promo_codes) and not course.discounted:
            discount_amount = (promo_code.discount_percentage/100) * item.purchase_price
            item.update_purchase_price(discount_amount)
            cart[item.course.id]['price'] = str(item.purchase_price)
