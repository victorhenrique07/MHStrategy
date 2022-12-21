from django.urls import path
from mhwapi import views

urlpatterns = [
    path('/', views.home, name="home"),
    path('monsters/', views.monsters, name="monsters"),
]