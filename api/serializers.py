from rest_framework import serializers
from .models import Product, Ingredient


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'product_type', 'title',
                  'image', 'description', 'price')


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = "__all__"
