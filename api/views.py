from django import http
from rest_framework.views import APIView
from .models import Product, Ingredient
from .serializers import ProductSerializer, IngredientSerializer
from rest_framework import generics, serializers, status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET"])
def get_products(request):
    data = ProductSerializer(Product.objects.all(), many=True).data
    return Response(data)


@api_view(["GET"])
def get_product(request, pk):
    data = ProductSerializer(Product.objects.get(id=pk)).data
    return Response(data)


class CreateProduct(APIView):

    def post(self, request):
        try:
            print("RAW: ", request.data)
            serialized = ProductSerializer(request.data)
            print("FROM SERIALIZER: ", serialized)
            if serialized.is_valid():
                serialized.save()
                Response(status=status.HTTP_201_CREATED)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
