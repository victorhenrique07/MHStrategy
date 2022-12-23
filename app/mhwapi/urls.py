from django.urls import path
from mhwapi import views

urlpatterns = [
    path('/', views.home, name="home"),
    path('monsters/', views.monsters, name="monsters"),
    path('monsters/<int:id>', views.get_monster, name="get monster"),
    path('monsters/create/<int:id>', views.register_monster, name="register monster")
]