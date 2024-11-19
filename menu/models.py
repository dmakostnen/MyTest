# menu/models.py
from django.db import models

class Dish(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='dishes/', null=True, blank=True)
    acctivate = models.BooleanField(default="true")

    def __str__(self):
        return self.name

class Order(models.Model):
    table_number = models.IntegerField()
    order_items = models.JSONField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Order {self.id}"
