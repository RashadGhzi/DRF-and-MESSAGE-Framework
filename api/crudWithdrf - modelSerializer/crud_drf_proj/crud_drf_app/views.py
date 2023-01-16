from django.shortcuts import render
import io
from .models import Student
from .serializer import StudentSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.
@csrf_exempt
def student_details(request):
    if request.method == 'GET':
        requestBody = request.body
        print(requestBody)
        print(type(requestBody))
        streamBody = io.BytesIO(requestBody)
        print(type(streamBody))
        pythonData = JSONParser().parse(streamBody)
        print(type(pythonData))
        id = pythonData.get('id',None)
        if id is not None:
            studentData = Student.objects.get(id=id)
            serializerData = StudentSerializer(studentData)
            jsonData = JSONRenderer().render(serializerData.data)
            return HttpResponse(jsonData, content_type = 'application/json')
        studentData= Student.objects.all()
        serializerData = StudentSerializer(studentData, many=True)
        jsonData= JSONRenderer().render(serializerData.data)
        return HttpResponse(jsonData, content_type='application/json')

    if request.method == 'POST':
        requestBody = request.body
        streamBody = io.BytesIO(requestBody)
        pythonData = JSONParser().parse(streamBody)
        serializerData = StudentSerializer(data=pythonData)
        if serializerData.is_valid():
            serializerData.save()
            resMsg = {'msg':'Your data has created'}
            jsonResData = JSONRenderer().render(resMsg['msg'])
            return HttpResponse(jsonResData, content_type='application/json')
        jsonResData = JSONRenderer().render(serializerData.errors)
        return HttpResponse(jsonResData, content_type = 'applicaton/json')

    if request.method == 'PUT':
        requestBody = request.body
        streamBody = io.BytesIO(requestBody)
        pythonData = JSONParser().parse(streamBody)
        id = pythonData.get('id')
        studentData = Student.objects.get(id=id)
        serializerData = StudentSerializer(studentData, data=pythonData, partial=True)
        if serializerData.is_valid():
            serializerData.save()
            resMsg = {'msg': 'Your data has updated'}
            jsonData = JSONRenderer().render(resMsg['msg'])
            return HttpResponse(jsonData, content_type='application/json')
        jsonData = JSONRenderer().render(serializerData.errors)
        return HttpResponse(jsonData, content_type='application/json')

    if request.method == 'DELETE':
        requestBody = request.body
        streamBody = io.BytesIO(requestBody)
        pythonData = JSONParser().parse(streamBody)
        id = pythonData.get('id')
        studentData = Student.objects.get(id=id)
        studentData.delete()
        resMsg = {'msg':'Your data has been deleted'}
        jsonData = JSONRenderer().render(resMsg['msg'])
        return HttpResponse(jsonData, content_type='application/json')
