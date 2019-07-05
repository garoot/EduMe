from decimal import Decimal
from django.conf import settings
from courses.models import Course


class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, course, quantity=1, update_quantity=False):
        course_id = str(course.id)
        if course_id not in self.cart:
            self.cart[course_id] = {'quantity': 0, 'price': str(course.course_price), 'name':course.course_name}
        if update_quantity:
            self.cart[course_id]['quantity'] = quantity
        else:
            self.cart[course_id]['quantity'] += quantity
        self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self, course):
        course_id = str(course.id)
        if course_id in self.cart:
            del self.cart[course_id]
            self.save()

    def __iter__(self):
        course_ids = self.cart.keys()
        courses = Course.objects.filter(id__in=course_ids)
        for course in courses:
            # course_data = {'price':str(course.course_price), 'name':str(course.course_name)}
            self.cart[str(course.id)]['course'] = course

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        sum=0
        for item in self.cart.values():
            sum += item['quantity']
        # return sum((item['quantity']) for item in self.cart.values())
        return sum

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def is_empty(self):
        sum = 0
        for item in self.cart.values():
            sum += 1
        if sum == 0:
            return True
        else:
            return False
    def print_items(self):
        for item in self.cart.values():
            print(item['name'])

    def items_ids(self):
        return self.cart.keys()

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
