# Generated by Django 4.2.1 on 2023-06-09 20:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0016_poi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='date_posted',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
