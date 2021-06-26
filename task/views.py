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


# Create your views here.
def Tasklist(request):
    return HttpResponse("hello")



def Index(request):
    return render(request, "task/compute.html")


def Nutrient(request):
    quantity = request.POST['quantity']

    spinach = [23, 3, 0.3, 8100, 93]

    if quantity.isdigit():
        quanti = int(quantity)
        totalspin = Compute().compute_nut(spinach, quanti)
        total = totalspin[0]

        return render(request, "task/food.html", {"result": total})
    else:
        res = "Only digits are allowed"
        return render(request, "task/food.html", {"result": res})


    # nutri = Nutrients.objects.all()
    # nutriform = NutrientsForm()
    # if request.method == "POST":
    #     nutrifom = NutrientsForm(request.POST)
    #     if nutrifom.is_valid():
    #         nutrifom.save()
    #     return redirect("/")

    # context = {'form': nutriform, 'nutri': nutri}
    # return render(request, "task/food.html", context)
