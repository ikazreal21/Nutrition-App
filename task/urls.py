from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutPage, name='logout'),



    path('', views.Index, name='dashboard'),
    path('compute', views.Calc,  name="food"),
    path('nutri', views.Nutrients, name="nutri"),
    path('foodlist/', views.Foodlist, name="foodlist"),
    path('addfood/', views.AddFood, name="addfood"),
    path("update/<str:pk>", views.UpFood, name="updateFood"),
    path("delete/<str:pk>", views.DelFood, name="deleteFood"),

]
