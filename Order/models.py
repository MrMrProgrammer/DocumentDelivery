from datetime import datetime
from django.db import models
from django.utils import timezone
from Store.models import Store


class ShippingMethod(models.Model):
    en_name = models.CharField(max_length=20)
    fa_name = models.CharField(max_length=20)

    def __str__(self):
        return self.fa_name

    class Meta:
        verbose_name = "Shipping Method"

    class Meta:
        verbose_name = 'Shipping Method'
        


class Order(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    order_number = models.TextField(blank=True, null=True)
    shipping_method = models.ForeignKey(ShippingMethod, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
    document_defects = models.CharField(max_length=200, blank=True, null=True)
    is_delete = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Order"

