from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.


class Nutrient(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    foodname = models.CharField(max_length=200)
    cal = models.IntegerField()
    protien = models.FloatField(max_length=20)
    fat = models.FloatField(max_length=20)
    vita = models.IntegerField()
    calcium = models.IntegerField()
    rndid = models.CharField(
        max_length=100, default=uuid.uuid4, editable=False, null=True, blank=True
    )

    def __str__(self):
        return self.foodname

    class Meta:
        ordering = ['foodname']
