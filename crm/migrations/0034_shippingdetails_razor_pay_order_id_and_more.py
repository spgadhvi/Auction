# Generated by Django 5.0.1 on 2024-02-12 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0033_remove_shippingdetails_shipping_details_submitted_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='shippingdetails',
            name='razor_pay_order_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='shippingdetails',
            name='razor_pay_payment_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='shippingdetails',
            name='razor_pay_payment_signature',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
