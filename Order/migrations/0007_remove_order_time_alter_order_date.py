# Generated by Django 4.2.7 on 2023-11-20 13:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0006_alter_order_order_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='time',
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
    ]
