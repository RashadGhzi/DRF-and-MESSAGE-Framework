
from django.contrib import admin
from django.urls import path
from .views import myappHome

urlpatterns = [
    path('', myappHome, name='myappHome'),
]