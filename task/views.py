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
    try:
        quantity = request.POST['quantity']
        pk = request.POST['foodid']
        if pk.isdigit():
            food = Nutrient.objects.get(id=pk)
            food1 = [food.cal, food.protien,
                       food.fat, food.vita, food.calcium]
            if quantity.isdigit():
                quanti = int(quantity)
                totalspin = Compute().compute_nut(food1, quanti)
                total = totalspin[0]

                return render(request, "task/compute.html", {"result": total})
            elif not quantity:
                return redirect('food')
            else:
                res = "Only digits are allowed"
                return render(request, "task/compute.html", {"result": res})
        elif not pk:
                return redirect('food')
        else:
            res = "Only digits are allowed"
            return render(request, "task/compute.html", {"result": res})

    except  Nutrient.DoesNotExist:
        res = "Do not in the Foodlist"
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
    food = Nutrient.objects.all()
    return render(request, "task/foodlist.html", {'food': food})


def AddFood(request):
    food = Nutrient.objects.all()
    foodform = NutrientsForm()
    if request.method == 'POST':
        foodform = NutrientsForm(request.POST)
        if foodform.is_valid():
            foodform.save()
        return redirect("foodlist")
    context = {'form': foodform, 'food': food}
    return render(request, "task/create.html", context)

def UpFood(request, pk):
    food = Nutrient.objects.get(id=pk)
    foodform = NutrientsForm(instance=food)

    if request.method == 'POST':
        foodform = NutrientsForm(request.POST, instance=food)
        if foodform.is_valid():
            foodform.save()
        return redirect('foodlist')
    return render(request, "task/update.html", {'form': foodform})


def DelFood(request, pk):
    food = Nutrient.objects.get(id=pk)
    if request.method == 'POST':
        food.delete()
        return redirect('foodlist')
    return render(request, "task/delete.html", {'food': food})


