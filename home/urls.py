from django.contrib import admin
from django.urls import path, include

# connecting views.py
from home import views

urlpatterns = [
    path("", views.index, name='home'),
    
]
