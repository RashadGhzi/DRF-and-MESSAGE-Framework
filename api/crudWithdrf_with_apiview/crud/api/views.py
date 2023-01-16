from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializer import StudentSerializer
from rest_framework import status
# Create your views here.

@api_view(['GET','POST','PUT','PATCH','DELETE'])
def student_details(request,id=None):
    if request.method == 'GET':
        if id is not None:
            studentData = Student.objects.get(pk = id)
            serializerData = StudentSerializer(studentData)
            return Response(serializerData.data, status=status.HTTP_200_OK)
        studentData = Student.objects.all()
        serializerData = StudentSerializer(studentData, many = True)
        return Response(serializerData.data, status=status.HTTP_200_OK)

    if request.method =='POST':
        data = request.data
        serializerData = StudentSerializer(data = data)
        if serializerData.is_valid():
            serializerData.save()
            return Response({'msg':'Deta created', 'data':request.data}, status=status.HTTP_200_OK)
        return Response(serializerData.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PATCH':
        id = id
        studentData = Student.objects.get(pk = id)
        serializerData = StudentSerializer(studentData, data=request.data, partial = True)
        if serializerData.is_valid():
            serializerData.save()
            return Response({'msg':'Data updated','data':request.data}, status=status.HTTP_202_ACCEPTED)
        return Response(serializerData.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'PUT':
        id = id
        studentData = Student.objects.get(pk = id)
        serializerData = StudentSerializer(studentData, data=request.data)
        if serializerData.is_valid():
            serializerData.save()
            return Response({'msg':'data updated', 'data':request.data}, status=status.HTTP_202_ACCEPTED)
        return Response(serializerData.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        id = id
        studentData = Student.objects.get(pk = id)
        studentData.delete()
        return Response({'msg':'data deleted'}, status=status.HTTP_200_OK)