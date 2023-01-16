from django.contrib import admin
from django.urls import path
from .views import student_details
urlpatterns = [
    path('student_details/', student_details),
    path('student_details/<int:id>', student_details)
]