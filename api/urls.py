from django.urls import path
from .views import get_products, get_product

urlpatterns = [
    path('products/', get_products),
    path('product/<pk>', get_product),
]
