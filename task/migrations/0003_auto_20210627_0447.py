# Generated by Django 3.2.4 on 2021-06-27 04:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_nutrients'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Nutrients',
            new_name='Nutrient',
        ),
        migrations.DeleteModel(
            name='Todo',
        ),
    ]
