from django.contrib.auth import get_user_model
from django.db import models
from products.models import Product


# Create your models here.
class Ticket(models.Model):
    STATUS_CHOICES = [
        ("O", "Open"),
        ("C", "Closed"),
    ]

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="O")
    table = models.CharField(max_length=10, null=True, blank=True)
    client_name = models.CharField(max_length=255, null=True, blank=True)
    client_phone = models.CharField(
        max_length=20, null=True, blank=True
    )  # TODO: Adicionar validator regexp
    observation = models.TextField(max_length=255, null=True, blank=True)
    bartender = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class TicketItem(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    # unit_value = models.DecimalField(max_digits=19, decimal_places=2)
    unit_value = models.DecimalField(
        Product.unit_value, max_digits=19, decimal_places=2
    )
