# Generated by Django 4.2.7 on 2023-11-20 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0004_alter_order_order_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='description',
        ),
        migrations.AddField(
            model_name='order',
            name='document_defects',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
