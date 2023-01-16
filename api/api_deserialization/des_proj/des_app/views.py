from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from .serializer import StudentSerializer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def student_create(request):
    if request.method == "POST":
        json_data = request.body
        print(json_data)
        stream = io.BytesIO(json_data)
        parser_data = JSONParser().parse(stream)
        serializer = StudentSerializer(data=parser_data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Data has created'}
            json_msg = JSONRenderer().render(res['msg'])
            return HttpResponse(json_msg, content_type = 'application/json')

    json_error = JSONRenderer().render(serializer.errors)
    return HttpResponse(json_error, content_type = 'application/json')