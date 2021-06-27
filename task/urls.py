from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index, name='dashboard'),
    path('compute', views.Calc,  name="food"),
    path('nutri', views.Nutrients, name="nutri"),
    path('foodlist', views.Foodlist, name="foodlist"),
    path('addfood', views.AddFood, name="addfood"),
    path("update/<str:pk>", views.UpFood, name="updateFood"),
    path("delete/<str:pk>", views.DelFood, name="deleteFood"),

]
