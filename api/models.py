from django.db import models


class Ingredient(models.Model):
    title = models.CharField(max_length=60)
    price = models.DecimalField(max_digits=100, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.title}"


class Product(models.Model):
    PRODUCT_TYPES = [
        ("DRINK", "Drink"),
        ("FOOD", "Food")
    ]
    product_type = models.CharField(max_length=30, choices=PRODUCT_TYPES)
    title = models.CharField(max_length=50)
    image = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=100, decimal_places=2)
    ingredients = models.ManyToManyField(Ingredient)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.title} ({self.product_type})"
