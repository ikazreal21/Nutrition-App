from django import forms
from django.forms import ModelForm
from .models import *


class NutrientsForm(forms.ModelForm):
    class Meta:
        model = Nutrients
        fields = "__all__"
