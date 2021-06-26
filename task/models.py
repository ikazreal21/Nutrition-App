from django.db import models

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['complete']


class Nutrients(models.Model):
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


