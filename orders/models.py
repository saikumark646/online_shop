from operator import itemgetter
from django.db import models
from my_app.models import Product
# Create your models here.

class Order(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    email = models.EmailField()
    postal_code = models.CharField(max_length=6)
    city = models.CharField(max_length=20)
    address = models.CharField(max_length=200, null = True,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    braintree_id = models.CharField(max_length=150, blank=True)
    
    def __str__(self):
        return f'Order {self.id}'
    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE,related_name='items')
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='order_items')
    price = models.DecimalField(max_digits=10,decimal_places=2)
    quantity = models.PositiveIntegerField(default = 1)
    
    def __str__(self):
        return str(self.id)
    def get_cost(self):
        return self.price * self.quantity