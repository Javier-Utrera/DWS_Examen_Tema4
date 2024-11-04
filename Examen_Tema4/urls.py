from django.urls import path
from django.contrib import admin
from .import views

# AQUI VAN LAS URLS

urlpatterns = [
    path('', views.index,name="urls_index"),    
]