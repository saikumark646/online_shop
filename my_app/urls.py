from django.urls import path
from . import views

app_name = 'my-app'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<slug:category_slug>/', views.product_list,
        name='product_list_by_category'),
    #path('product/<int:id>/', views.product_detail, name='product_detail')
    path('<slug>/<int:id>/', views.product_detail, name='product_detail')
    
]
