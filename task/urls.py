from django.contrib.auth import views as auth_views

from django.urls import path
from . import views

urlpatterns = [
    # User
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutPage, name='logout'),
    # App
    path('', views.Index, name='dashboard'),
    path('compute/', views.Calc, name="food"),
    path('nutri', views.Nutrients, name="nutri"),
    path('foodlist/', views.Foodlist, name="foodlist"),
    path("about/", views.About, name='about'),
    path('addfood/', views.AddFood, name="addfood"),
    path("update/<str:pk>", views.UpFood, name="updateFood"),
    path("delete/<str:pk>", views.DelFood, name="deleteFood"),
    # Reset Pass
    path(
        'reset_password/',
        auth_views.PasswordResetView.as_view(template_name="task/password_reset.html"),
        name='reset_password',
    ),
    path(
        'reset_password_sent/',
        auth_views.PasswordResetDoneView.as_view(
            template_name="task/password_reset_sent.html"
        ),
        name='password_reset_done',
    ),
    path(
        'reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name="task/password_reset_form.html"
        ),
        name='password_reset_confirm',
    ),
    path(
        'reset_password_complete/',
        auth_views.PasswordResetCompleteView.as_view(
            template_name="task/password_reset_done.html"
        ),
        name='password_reset_complete',
    ),
]
