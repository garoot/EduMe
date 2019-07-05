# from celery import Celery
from courses.models import Order
from celery import task
from django.core.mail import send_mail
# app = Celery('tasks', broker='pyamqp://guest@localhost//')

# @app.task
@task
def order_created(order_id):
    order = Order.objects.get(id=order_id)
    user = order.profile.user
    subject = 'Order no. {}'.format(order.id)
    message = 'Dear {},\n\nYou have successfully placed an order.\
                Your order number: {}\n\nThank you,\nEduMe'.format(user.first_name, order.id)
    mail_sent = send_mail(subject, message, 'majeed.garoot@gmail.com', user.email)

    return mail_sent
