# Generated by Django 4.2.1 on 2023-06-02 15:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0013_alter_property_date_posted'),
    ]

    operations = [
        migrations.RenameField(
            model_name='property',
            old_name='seller',
            new_name='user',
        ),
    ]
