
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('student_details/',StudentApi.as_view()),
]