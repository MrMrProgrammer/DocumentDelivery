# Generated by Django 4.2.7 on 2023-11-09 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.IntegerField()),
                ('shipping_method', models.CharField(choices=[('post', 'post'), ('tipax', 'tipax'), ('delivery', 'delivery')], max_length=20)),
            ],
        ),
    ]
