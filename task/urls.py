from django.urls import path
from . import views

urlpatterns = [
    # path('', views.Tasklist, name='home'),
    path('', views.Index,  name="food"),
    path('nutri', views.Nutrient, name="nutri")
]
