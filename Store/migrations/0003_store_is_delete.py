# Generated by Django 4.2.7 on 2023-12-02 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0002_store_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='is_delete',
            field=models.BooleanField(default=False),
        ),
    ]
