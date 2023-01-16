from django.shortcuts import render
from .models import Students
from .serializer import StudentSerializer
from rest_framework.renderers import JSONRenderer
import io
from rest_framework.parsers import JSONParser
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
# Create your views here.
@method_decorator(csrf_exempt, name='dispatch')
class StudentApi(View):
    def get(self, request, *args, **kwargs):
        bodyData = request.body
        streamData = io.BytesIO(bodyData)
        pythonData = JSONParser().parse(streamData)
        id = pythonData.get('id', None)
        if id is not None:
            studentData = Students.objects.get(id = id)
            serializerData = StudentSerializer(studentData)
            jsonData = JSONRenderer().render(serializerData.data)
            return HttpResponse(jsonData, content_type='application/json')
        studentData = Students.objects.all()
        serializerData = StudentSerializer(studentData, many=True)
        jsonData = JSONRenderer().render(serializerData.data)
        return HttpResponse(jsonData,content_type='application/json')

    def post(self, request, *args, **kwargs):
        bodyData = request.body
        # print(bodyData)
        streamData = io.BytesIO(bodyData)
        pythonData = JSONParser().parse(streamData)
        serializerData = StudentSerializer(data = pythonData)
        if serializerData.is_valid():
            serializerData.save()
            res = {'msg':'Data has created'}
            res_json_data = JSONRenderer().render(res['msg'])
           
            return HttpResponse(res_json_data,content_type='application/json')
        # ser_data_check = serializerData.errors
        res_json_data = JSONRenderer().render(serializerData.errors)
        print(res_json_data)
        return HttpResponse(res_json_data, content_type='application/json')
    
    def updat(self, request, *args, **kwargs):
        bodyData = request.body
        # print(bodyData)
        streamData = io.BytesIO(bodyData)
        # print(streamData)
        pythonData = JSONParser().parse(streamData)
        print(pythonData)
        id = pythonData.get('id')
        # print(id)
        studentData = Students.objects.get(id=id)
        # Complete data - Required all data from front end/ client
        # serializerData = StudentSerializer(studentData, data=pythonData, partial=True) #  This is for partial update
        # Partial Data - All data not required
        serializerData = StudentSerializer(studentData, data=pythonData, partial=True)  #  This is for complete update 
        if serializerData.is_valid():
            serializerData.save()
            res = {'msg':'Data has uprdated'}
            res_json_data = JSONRenderer().render(res['msg'])
            return HttpResponse(res_json_data, content_type='application/json')
        
        res_json_data = JSONRenderer().render(serializerData.errors)
        print(res_json_data)
        return HttpResponse(res_json_data, content_type='application/json')

    def delete(self, request, *args, **kwargs):
        bodyData = request.body
        streamData = io.BytesIO(bodyData)
        pythonData = JSONParser().parse(streamData)
        id = pythonData.get('id')
        studentData = Students.objects.get(id=id)
        studentData.delete()
        res = {'msg':'Your data has deleted'}
        res_json_data = JSONRenderer().render(res['msg'])
        print(res_json_data)
        return HttpResponse(res_json_data, content_type='application/json')

        
