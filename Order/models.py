from django.db import models
from Store.models import Store


class Order(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    order_number = models.IntegerField(blank=True, null=True)
    shipping_methods = (
        ("post", "پست"),
        ("tipax", "تیپاکس"),
        ("delivery", "پیک موتوری"),
    )
    shipping_method = models.CharField(max_length=20, choices=shipping_methods, null=True, blank=True)
    date = models.DateField(auto_now_add=True, null=True)
    time = models.TimeField(auto_now_add=True, null=True)
    description = models.TextField(null=True, blank=True)
