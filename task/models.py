from django.db import models

# Create your models here.

class Nutrient(models.Model):
    foodname = models.CharField(max_length=200)
    cal = models.FloatField(max_length=20)
    protien = models.FloatField(max_length=20)
    fat = models.FloatField(max_length=20)
    vita = models.FloatField(max_length=20)
    calcium = models.FloatField(max_length=20)

    def __str__(self):
        return self.foodname
    
    class Meta:
        ordering = ['foodname']


