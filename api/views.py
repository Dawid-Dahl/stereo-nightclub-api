from .models import Product, Ingredient
from .serializers import ProductSerializer, IngredientSerializer
from rest_framework import generics, serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET"])
def get_products(request):
    print(request)
    data = ProductSerializer(Product.objects.all(), many=True).data
    return Response(data)
