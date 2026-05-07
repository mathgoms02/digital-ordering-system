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


class Ticket(models.Model):
    STATUS_CHOICES = [
        ("O", "Open"),
        ("C", "Closed"),
    ]

    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    table = models.CharField(max_length=10)
    client_name = models.CharField(max_length=255)
    client_phone = models.CharField(max_length=20) # TODO: Adicionar validator regexp
    observation = models.CharField(max_length=255)
    # bartender = models.ForeignKey(Users, on_delete=models.CASCADE) TODO: Create Model User
    created_at = models.DateTimeField(auto_now_add=True)


class TicketItem(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    unit_value = models.DecimalField(max_digits=19, decimal_places=2)
