from django.shortcuts import render
from .models import Students
from .serializer import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
# Create your views here.


# query set all student data
def student_details(request, pk):
    stu = Students.objects.get(id = pk)     # complex data
    serializer = StudentSerializer(stu)     # complex data converted to python native data
    # serializer = StudentSerializer(stu, many=True)     # complex data converted to python native data
    # json_data = JSONRenderer().render(serializer.data)      # python native data converted to  JSON data
    # return HttpResponse(json_data, content_type='application/json') 
    return JsonResponse(serializer.data, safe=False)