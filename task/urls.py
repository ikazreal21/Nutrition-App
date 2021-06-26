from django.urls import path
from . import views

urlpatterns = [
    path('', views.Tasklist, name='home'),
    path('food/', views.Nutrient, name='meal')
]
