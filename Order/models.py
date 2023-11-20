from datetime import datetime
from django.db import models
from django.utils import timezone

from Store.models import Store


class Order(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    order_number = models.TextField(blank=True, null=True)
    shipping_methods = (
        ("post", "پست"),
        ("tipax", "تیپاکس"),
        ("delivery", "پیک موتوری"),
    )
    shipping_method = models.CharField(max_length=20, choices=shipping_methods, null=True, blank=True)
    date = models.DateTimeField(default=timezone.now, null=True)
    # time = models.TimeField(auto_now_add=True, null=True)
    # description = models.TextField(null=True, blank=True)
    document_defects = models.CharField(max_length=200, blank=True, null=True)