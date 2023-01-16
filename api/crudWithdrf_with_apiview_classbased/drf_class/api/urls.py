from django.contrib import admin
from django.urls import path
from .views import StudentAPI
urlpatterns = [
    path('student_details/', StudentAPI.as_view()),
    path('student_details/<int:pk>/', StudentAPI.as_view()),
]
