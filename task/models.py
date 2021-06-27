from django.db import models

# Create your models here.

class Nutrient(models.Model):
    foodname = models.CharField(max_length=200)
    cal = models.IntegerField()
    protien = models.FloatField(max_length=20)
    fat = models.FloatField(max_length=20)
    vita = models.IntegerField()
    calcium = models.IntegerField()

    def __str__(self):
        return self.foodname
    
    class Meta:
        ordering = ['foodname']


