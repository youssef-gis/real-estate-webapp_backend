# Generated by Django 4.2.1 on 2023-05-25 09:46

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True)),
                ('areas', models.CharField(blank=True, choices=[('Inner London', 'Inner London'), ('Outer London', 'Outer London')], max_length=20, null=True)),
                ('borough', models.CharField(blank=True, max_length=50, null=True)),
                ('property_type', models.CharField(blank=True, choices=[('House', 'House'), ('Apartment', 'Apartment'), ('Office', 'office')], max_length=50, null=True)),
                ('property_status', models.CharField(blank=True, choices=[('sale', 'sale'), ('rent', 'rent')], max_length=50, null=True)),
                ('price', models.DecimalField(decimal_places=0, max_digits=5)),
                ('rental_frequency', models.CharField(blank=True, choices=[('Month', 'Month'), ('Week', 'Week'), ('Day', 'Day')], max_length=20, null=True)),
                ('rooms', models.IntegerField(blank=True, null=True)),
                ('furnished', models.BooleanField(default=False)),
                ('pool', models.BooleanField(default=False)),
                ('elevator', models.BooleanField(default=False)),
                ('cctv', models.BooleanField(default=False)),
                ('parking', models.BooleanField(default=False)),
                ('date_posted', models.DateField(default=django.utils.timezone.now)),
                ('location', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326)),
            ],
        ),
    ]