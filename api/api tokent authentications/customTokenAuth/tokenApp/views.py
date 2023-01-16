from django.shortcuts import render
from .serializer import StudentSerializer
from .models import Student
from rest_framework import viewsets
# Create your views here.
class StudentDetails(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer