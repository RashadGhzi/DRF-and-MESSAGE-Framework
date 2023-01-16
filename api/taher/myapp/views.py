from django.shortcuts import render, HttpResponse
from .models import Student
from .serializer import StudentSerializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db.models import F

# Create your views here.
@api_view(['GET','POST','PUT','PATCH'])
def student(request,id=None):
    if request.method=='GET':
        if id is not None:
            studentdata = Student.objects.get(pk=id)
            serializerdata = StudentSerializers(studentdata)
            return Response(serializerdata.data)

        studentdata = Student.objects.annotate(odd=F('id')%2).filter(odd=False)
        serializerdata = StudentSerializers(studentdata, many=True)
        return Response(serializerdata.data)

    if request.method == 'POST':
        data = request.data
        comlexData = StudentSerializers(data=data)
        if comlexData.is_valid():
            comlexData.save()
            return Response({'msg':'Data created'})
        else:
            return Response(comlexData.errors)
    
    if request.method == 'PUT':
        studentdata = Student.objects.get(pk=id)
        serializerdata = StudentSerializers(studentdata, data=request.data)
        if serializerdata.is_valid():
            serializerdata.save()
            return Response({'message':'data update'})
        else:
            return Response(serializerdata.errors)
    if request.method=='PATCH':
        data = request.data
        studentdata = Student.objects.get(pk=id)
        serializerdata = StudentSerializers(studentdata, data=data, partial=True)
        if serializerdata.is_valid():
            serializerdata.save()
            return Response({'message':'update done'})

        else: 
            return Response(serializerdata.errors)