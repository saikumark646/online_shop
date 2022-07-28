from django.urls import path
from .views import payment_canceled,payment_process,payment_done

app_name = 'payment'

urlpatterns = [
    path('process/',payment_process,name = 'process'  ),
    path('done/',payment_done, name = 'done'),
    path('canceled/',payment_canceled, name = 'canceled')

]
