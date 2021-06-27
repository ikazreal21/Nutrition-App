from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index, name='dashboard'),
    path('compute', views.Calc,  name="food"),
    path('nutri', views.Nutrients, name="nutri"),
    path('foodlist', views.Foodlist, name="foodlist"),
]
