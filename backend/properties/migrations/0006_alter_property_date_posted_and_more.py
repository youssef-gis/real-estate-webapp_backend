# Generated by Django 4.2.1 on 2023-05-30 20:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0005_remove_property_location_property_latitude_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='date_posted',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='property',
            name='property_status',
            field=models.CharField(blank=True, choices=[('Sale', 'Sale'), ('Rent', 'Rent')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='property_type',
            field=models.CharField(blank=True, choices=[('House', 'House'), ('Appartment', 'Appartment'), ('Office', 'Office')], max_length=50, null=True),
        ),
    ]
