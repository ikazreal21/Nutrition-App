# Generated by Django 3.2.4 on 2021-07-01 19:32

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0006_nutrient_randid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nutrient',
            name='randid',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]
