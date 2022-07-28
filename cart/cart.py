from django.conf import settings
from decimal import Decimal
from my_app.models import Product

class Cart(object):
    def __init__(self,request): #Initialize the cart.
        self.session = request.session #storing the current session
        cart = self.session.get(settings.CART_SESSION_ID)  
        #trying to get the cart from the current session 
        if not cart:  #save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart
        
    def add(self,product,quantity =1,override_quantity = False):
        product_id = str(product.id) 
        # int is converted to str why because django uses JSON to serialize the session data, json accepts only string key names.product_id is taken as key
        if product_id not in self.cart:
            self.cart[product_id] = {
                                'quantity':0,
                                'price':str(product.price)
            }
        elif override_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()
    def save(self):
        self.session.modified = True
        ## mark the session as "modified" to make sure it gets saved
    def remove(self,product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()
        
    def __iter__(self): 
        product_id = self.cart.keys()
        products = Product.objects.filter(id__in = product_id)
        cart = self.cart.copy() # You copy the current cart in the cart
        for product in products: 
            # product instances is added to cart
            cart[str(product.id)]['product'] = product 
            # in cart {'5':{'product':<QuerySet [<Product: fitness training>]>}}
        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item
            
    def __len__(self):
        #Count all items in the cart.
        return sum(item['quantity'] for item in self.cart.values())
    
    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())
    
    def clear(self):
        # remove cart from session
        del self.session[settings.CART_SESSION_ID]
        self.save()