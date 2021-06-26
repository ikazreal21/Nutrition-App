from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *


class Compute():
    def __init__(self):
        self.Total = []

    def compute_nut(self, food, quantity):
        for i in food:
            self.Total.append(i*quantity)
        return self.Total


# Create your views here.
def Tasklist(request):
    return HttpResponse("hello")


def Nutrient(request):
    nutri = Nutrients.objects.all()
    nutriform = NutrientsForm()
    if request.method == "POST":
        nutrifom = NutrientsForm(request.POST)
        if nutrifom.is_valid():
            nutrifom.save()
        return redirect("/")

    context = {'form': nutriform, 'nutri': nutri}
    return render(request, "task/food.html", context)
