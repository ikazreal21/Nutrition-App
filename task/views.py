from django.shortcuts import render, redirect
from django.utils.datastructures import MultiValueDictKeyError
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required

import requests, zulu, os

from dotenv import load_dotenv
load_dotenv()

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


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, "Account Created For " + user)
                return redirect('login')

        context = {"form": form}
        return render(request, "task/register.html", context)



def loginPage(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        if request.method == 'POST':
           username = request.POST.get('username')
           password = request.POST.get('password')
           user = authenticate(request, username=username, password=password)
           if user is not None:
            login(request, user)
            return redirect('dashboard')
           else:
            messages.info(request, "Username or Password is Incorrect")

    context = {}
    return render(request, "task/login.html", context)


def logoutPage(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def Index(request):
    APIKEY = database_url = os.environ.get('APIKEY')
    newsresponse = requests.get(url='https://newsapi.org/v2/top-headlines?country=ph&category=health&apiKey={}'.format(APIKEY))
    newsresponse = newsresponse.json()
    if newsresponse["status"] != "ok":
        return HttpResponse("<h1>Request Failed</h1>")
    newsresponse = newsresponse['articles']

    context = {
        "data": []
    }

    for i in newsresponse:
        dt = zulu.parse(i["publishedAt"])
        context["data"].append({
            "title": i["title"],
            "description": "" if i["description"] is None else i["description"],
            "url": i["url"],

            "publishedat": dt.time_from_now()
        })
    return render(request, "task/dashboard.html", context)


@login_required(login_url='login')
def Calc(request):
    food = Nutrient.objects.filter(user=request.user)
    return render(request, "task/compute.html", {"food": food})


# Need to Refactor To Many Repeating Codes
@login_required(login_url='login')
def Nutrients(request):
    try:
        quantity1 = request.POST['quantity1']
        pk1 = request.POST['food1']
        quantity2 = request.POST['quantity2']
        pk2 = request.POST['food2']
        quantity3 = request.POST['quantity3']
        pk3 = request.POST['food3']
        quantity4 = request.POST['quantity4']
        pk4 = request.POST['food4']
        quantity5 = request.POST['quantity5']
        pk5 = request.POST['food5']
        quantity6 = request.POST['quantity6']
        pk6 = request.POST['food6']
        quantity7 = request.POST['quantity7']
        pk7 = request.POST['food7']
        quantity8 = request.POST['quantity8']
        pk8 = request.POST['food8']
        quantity9 = request.POST['quantity9']
        pk9 = request.POST['food9']
        quantity10 = request.POST['quantity10']
        pk10 = request.POST['food10']
    except MultiValueDictKeyError:
        return redirect("food")

    if pk1.isdigit() or pk2.isdigit() or pk3.isdigit() or pk4.isdigit() or pk5.isdigit() or pk6.isdigit() or pk7.isdigit() or pk8.isdigit() or pk9.isdigit() or pk10.isdigit():
        food1 = Nutrient.objects.get(id=pk1)
        food1 = [food1.cal, food1.protien,
                 food1.fat, food1.vita, food1.calcium]
        food2 = Nutrient.objects.get(id=pk2)
        food2 = [food2.cal, food2.protien,
                 food2.fat, food2.vita, food2.calcium]
        food3 = Nutrient.objects.get(id=pk3)
        food3 = [food3.cal, food3.protien,
                 food3.fat, food3.vita, food3.calcium]
        food4 = Nutrient.objects.get(id=pk4)
        food4 = [food4.cal, food4.protien,
                 food4.fat, food4.vita, food4.calcium]
        food5 = Nutrient.objects.get(id=pk5)
        food5 = [food5.cal, food5.protien,
                 food5.fat, food5.vita, food5.calcium]
        food6 = Nutrient.objects.get(id=pk6)
        food6 = [food6.cal, food6.protien,
                 food6.fat, food6.vita, food6.calcium]
        food7 = Nutrient.objects.get(id=pk7)
        food7 = [food7.cal, food7.protien,
                 food7.fat, food7.vita, food7.calcium]
        food8 = Nutrient.objects.get(id=pk8)
        food8 = [food8.cal, food8.protien,
                 food8.fat, food8.vita, food8.calcium]
        food9 = Nutrient.objects.get(id=pk9)
        food9 = [food9.cal, food9.protien,
                 food9.fat, food9.vita, food9.calcium]
        food10 = Nutrient.objects.get(id=pk10)
        food10 = [food10.cal, food10.protien,
                  food10.fat, food10.vita, food10.calcium]
        # return render(request, "task/compute.html", {"result": food})
        if quantity1.isdigit() and quantity2.isdigit() and quantity3.isdigit() and quantity4.isdigit() and quantity5.isdigit() and quantity6.isdigit() and quantity7.isdigit() and quantity8.isdigit() and quantity9.isdigit() and quantity10.isdigit():
            quanti1 = int(quantity1)
            quanti2 = int(quantity2)
            quanti3 = int(quantity3)
            quanti4 = int(quantity4)
            quanti5 = int(quantity5)
            quanti6 = int(quantity6)
            quanti7 = int(quantity7)
            quanti8 = int(quantity8)
            quanti9 = int(quantity9)
            quanti10 = int(quantity10)

            total1 = Compute().compute_nut(food1, quanti1)
            total2 = Compute().compute_nut(food2, quanti2)
            total3 = Compute().compute_nut(food3, quanti3)
            total4 = Compute().compute_nut(food4, quanti4)
            total5 = Compute().compute_nut(food5, quanti5)
            total6 = Compute().compute_nut(food6, quanti6)
            total7 = Compute().compute_nut(food7, quanti7)
            total8 = Compute().compute_nut(food8, quanti8)
            total9 = Compute().compute_nut(food9, quanti9)
            total10 = Compute().compute_nut(food10, quanti10)

            cal = total1[0]+total2[0]+total3[0]+total4[0]+total5[0] + \
                total6[0]+total7[0]+total8[0]+total9[0]+total10[0]
            pro = total1[1]+total2[1]+total3[1]+total4[1]+total5[1] + \
                total6[1]+total7[1]+total8[1]+total9[1]+total10[1]
            fat = total1[2]+total2[2]+total3[2]+total4[2]+total5[2] + \
                total6[2]+total7[2]+total8[2]+total9[2]+total10[2]
            vit = total1[3]+total2[3]+total3[3]+total4[3]+total5[3] + \
                total6[3]+total7[3]+total8[3]+total9[3]+total10[3]
            calc = total1[4]+total2[4]+total3[4]+total4[4]+total5[4] + \
                total6[4]+total7[4]+total8[4]+total9[4]+total10[4]
            context = {'cal': cal, 'pro': pro,
                       'fat': fat, 'vit': vit, 'calc': calc}

            return render(request, "task/compute.html", context)
        elif not quantity1 or not quantity2 or not quantity3 or not quantity4 or not quantity5 or not quantity6 or not quantity7 or not quantity8 or not quantity9 or not quantity10:
            res = "All Fields are Required"
            return render(request, "task/compute.html", {"res": res})
        else:
            res = "Only digits are allowed"
            return render(request, "task/compute.html", {"res": res})
    elif pk1 is None or pk2 is None or pk3 is None  or pk4 is None  or pk5 is None  or pk6 is None  or pk7 is None  or pk8 is None  or pk9 is None  or pk10 is None :
        res = "All Fields are Required"
        return render(request, "task/compute.html", {"res": res})
    else:
        res = "Only digits are allowed"
        return render(request, "task/compute.html", {"res": res})

    # nutri = Nutrients.objects.all()
    # nutriform = NutrientsForm()
    # if request.method == "POST":
    #     nutrifom = NutrientsForm(request.POST)
    #     if nutrifom.is_valid():
    #         nutrifom.save()
    #     return redirect("/")

    # context = {'form': nutriform, 'nutri': nutri}
    # return render(request, "task/food.html", context)

@login_required(login_url='login')
def Foodlist(request):
    food = Nutrient.objects.filter(user=request.user)
    return render(request, "task/foodlist.html", {'food': food})

@login_required(login_url='login')
def AddFood(request):
    foodform = NutrientsForm()
    if request.method == 'POST':
        foodform = NutrientsForm(request.POST)
        if foodform.is_valid():
            foodform.save(commit=False).user = request.user
            foodform.save()
        return redirect("foodlist")
    context = {'form': foodform}  
    return render(request, "task/create.html", context)

@login_required(login_url='login')
def UpFood(request, pk):
    food = Nutrient.objects.get(rndid=pk)
    foodform = NutrientsForm(instance=food)

    if request.method == 'POST':
        foodform = NutrientsForm(request.POST, instance=food)
        if foodform.is_valid():
            foodform.save()
        return redirect('foodlist')
    return render(request, "task/update.html", {'form': foodform})

@login_required(login_url='login')
def DelFood(request, pk):
    food = Nutrient.objects.get(rndid=pk)
    if request.method == 'POST':
        food.delete()
        return redirect('foodlist')
    return render(request, "task/delete.html", {'food': food})
