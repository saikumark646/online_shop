#Setting the cart into the request context
#will be able to access the cart in any template and add context_processor to the templates in the settings.p




from .cart import Cart

def cart(request):
    return { 'cart': Cart(request) }