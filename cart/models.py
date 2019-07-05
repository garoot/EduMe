from django.db import models
from django.utils import timezone
from courses.models import Course, CourseReport, OrderItem, Order

# 
# # Create your models here.
#
# class Order(models.Model):
#     profile = models.ForeignKey('accounts.Profile', on_delete=models.CASCADE, related_name='orders')
#
#     """
#     - Purchase date is automatically adjusted to "today's date" upon the completion of a purchase
#     - It will be copied to the payment information email
#     - it's not to be adjusted by customers
#     """
#     purchase_date = models.DateTimeField(default=timezone.now, editable=False, blank=True)
#     """
#     - Total amount is instantly updated when a course is added or removed from the list
#     """
#     total_amount = models.FloatField(blank=True)
#
# class PromotionCode(models.Model):
#     course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="promo_codes")
#     code = models.CharField(max_length=10, unique=True, primary_key=True )
#     valid_from = models.DateTimeField()
#     valid_to = models.DateTimeField()
#     active = models.BooleanField()
#     uses = models.IntegerField(null=True)
# """
# When the user adds a course to the order list, OrderItem is created
# """
# class OrderItem(models.Model):
#     order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
#     course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
#     """
#     - when a course is added to the order list, we check if the promotion code field is valid
#     - Then based on the promotion we adjust the price of the order item
#     - Then we update the total price of the order
#     """
#     purchase_price =models.FloatField(blank=True)
#     course_report = models.ForeignKey(CourseReport, on_delete=models.SET_NULL, related_name="order_item", null=True)
#
#     def update_purchase_price(discount_amount):
#         self.purchase_price = course.course_price - discount_amount
