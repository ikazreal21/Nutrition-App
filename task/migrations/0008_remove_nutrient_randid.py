# Generated by Django 3.2.4 on 2021-07-01 19:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0007_alter_nutrient_randid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nutrient',
            name='randid',
        ),
    ]
