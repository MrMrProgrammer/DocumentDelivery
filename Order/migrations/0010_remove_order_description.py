# Generated by Django 4.2.7 on 2023-12-10 11:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0009_shippingmethod_alter_order_shipping_method'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='description',
        ),
    ]