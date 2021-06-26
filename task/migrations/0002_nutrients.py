# Generated by Django 3.2.4 on 2021-06-26 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nutrients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foodname', models.CharField(max_length=200)),
                ('cal', models.FloatField(max_length=20)),
                ('protien', models.FloatField(max_length=20)),
                ('fat', models.FloatField(max_length=20)),
                ('vita', models.FloatField(max_length=20)),
                ('calcium', models.FloatField(max_length=20)),
            ],
            options={
                'ordering': ['foodname'],
            },
        ),
    ]