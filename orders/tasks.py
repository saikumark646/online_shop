# from celery import task
# from django.core.mail import send_mail
# from .models import Order
# @task
# def order_created(order_id):
#     order = Order.objects.get(id=order_id)
#     subject = f'Order nr. {order.id}'
#     message = f'Dear {order.firstname},\n\n' \
#     f'You have successfully placed an order.' \
#     f'Your order ID is {order.id}.'
#     mail_sent = send_mail(subject,
#     message,
#     'admin@myshop.com',
#     [order.email])
#     return mail_sent

# """
# The CELERY_ALWAYS_EAGER setting allows you to execute tasks
# locally in a synchronous way, instead of sending them to the queue.
# This is useful for running unit tests or executing the application in
# your local environment without running Celery.
# Building an Online Shop
# [ 266 ]
# Task to send an e-mail notification when an order is
# successfully created.
# """