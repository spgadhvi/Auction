# Generated by Django 5.0.1 on 2024-02-08 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0023_remove_product_highest_bid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='min_price',
            field=models.DecimalField(decimal_places=2, default=2000, max_digits=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='price_interval',
            field=models.DecimalField(decimal_places=2, default=100, max_digits=10),
        ),
    ]
