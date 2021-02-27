from rest_framework import serializers
from .models import Product, Ingredient


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("id", "product_type", "title", "image", "description",
                  "price", "ingredients", "created_at", "updated_at")


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ("id", "title", "price", "created_at", "updated_at")
