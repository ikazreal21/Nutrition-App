# Generated by Django 3.2.4 on 2021-07-04 15:29

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0010_remove_nutrient_randid'),
    ]

    operations = [
        migrations.AddField(
            model_name='nutrient',
            name='rndid',
            field=models.CharField(blank=True, default=uuid.uuid4, editable=False, max_length=100, null=True),
        ),
    ]
