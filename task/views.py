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


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def Index(request):
    return render(request, "task/dashboard.html")


def Calc(request):
    return render(request, "task/compute.html")


def Nutrients(request):
    quantity = request.POST['quantity']
    spinach = Nutrient.objects.get(pk=1)
    spinach = [spinach.cal, spinach.protien,
               spinach.fat, spinach.vita, spinach.calcium]

    if quantity.isdigit():
        quanti = int(quantity)
        totalspin = Compute().compute_nut(spinach, quanti)
        total = totalspin[2]

        return render(request, "task/compute.html", {"result": total})
    elif not quantity:
        return redirect('food')
    else:
        res = "Only digits are allowed"
        return render(request, "task/compute.html", {"result": res})

    # nutri = Nutrients.objects.all()
    # nutriform = NutrientsForm()
    # if request.method == "POST":
    #     nutrifom = NutrientsForm(request.POST)
    #     if nutrifom.is_valid():
    #         nutrifom.save()
    #     return redirect("/")

    # context = {'form': nutriform, 'nutri': nutri}
    # return render(request, "task/food.html", context)


def Foodlist(request):
    return render(request, "task/foodlist.html")
