from rest_framework import serializers
from .models import Product, Ingredient


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('title', 'price')


class ProductSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(read_only=True, many=True)

    class Meta:
        model = Product
        fields = ('id', 'product_type', 'title',
                  'image', 'description', 'price', 'ingredients')
