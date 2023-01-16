from django.shortcuts import render
from .models import Student
from .serializer import StudentSerializer
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView,DestroyAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.
class StudentLC(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]