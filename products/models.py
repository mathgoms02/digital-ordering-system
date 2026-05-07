from django.db import models

# Create your models here.
class Product(models.Model):
    PRODUCTS_CATEGORY = [
        ("F", "Food"),
        ("D", "Drink"),
        ("O", "Other")
    ]

    name = models.CharField(max_length=255)
    category = models.CharField(max_length=30, choices=PRODUCTS_CATEGORY)
    # Decimal is better to work with money
    unit_value = models.DecimalField(max_digits=19, decimal_places=2)
