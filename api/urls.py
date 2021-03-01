from django.urls import path
from .views import CreateProduct, get_products, get_product

urlpatterns = [
    path('products/', get_products),
    path('product/<pk>', get_product),
    path('products/create/', CreateProduct.as_view()),
]
