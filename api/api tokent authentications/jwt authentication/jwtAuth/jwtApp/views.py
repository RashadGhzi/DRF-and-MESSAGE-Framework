from django.shortcuts import render
from .serializer import StudentSerializer
from .models import Student
from rest_framework import viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.
class StudentDetails(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

# list 
# dictionary
# tuple 
# orm 
# django 
# rest api 
# jwt 
# oop
# orm vs row query 
# annotate
# itertools
# literals