from django import http
from django.db.models import query
from django.http.response import JsonResponse
from rest_framework.views import APIView
from rest_framework.generics import DestroyAPIView
from .models import Product, Ingredient
from .serializers import ProductSerializer, IngredientSerializer
from rest_framework import generics, serializers, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json


@api_view(["GET"])
def get_products(request):
    data = ProductSerializer(Product.objects.all(), many=True).data
    return Response(data)


@api_view(["GET"])
def get_product(request, pk):
    data = ProductSerializer(Product.objects.get(id=pk)).data
    return Response(data)


class CreateProduct(APIView):
    serializer_class = ProductSerializer

    def post(self, request):
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)


class DeleteProduct(DestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"msg": "Item has been deleted!"})
