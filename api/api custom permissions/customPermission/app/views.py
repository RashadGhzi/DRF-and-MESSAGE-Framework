from django.shortcuts import render
from .serializer import StudentSerializer
from .models import Student
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.authentication import SessionAuthentication
from .custompermission import CusPermission
from rest_framework.permissions import IsAuthenticated
# Create your views here.
class StudentLC(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [CusPermission]
class StudentRUD(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [CusPermission,IsAuthenticated]