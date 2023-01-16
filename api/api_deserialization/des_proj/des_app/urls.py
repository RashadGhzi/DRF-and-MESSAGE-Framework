
from django.contrib import admin
from django.urls import path
from .views import student_create
urlpatterns = [
    path('stddes/', student_create, name='stddes')
]
