from django.shortcuts import render
from .serializer import StudentSerializer
from .models import Student
from rest_framework.views import APIView
# from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
# @api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])


class StudentAPI(APIView):
    def get(self, request, pk=None, format=None):
        pk = pk
        if pk is not None:
            studentData = Student.objects.get(pk=pk)
            serializerData = StudentSerializer(studentData)
            return Response(serializerData.data, status=status.HTTP_200_OK)

        studentData = Student.objects.all()
        serializerData = StudentSerializer(studentData, many=True)
        return Response(serializerData.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        data = request.data
        serializerData = StudentSerializer(data=data)
        if serializerData.is_valid():
            serializerData.save()
            return Response({'msg': 'data created', 'data': request.data}, status=status.HTTP_201_CREATED)
        return Response(serializerData.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None, format=None):
        id = pk
        studentData = Student.objects.get(pk=id)
        serializerData = StudentSerializer(studentData, data=request.data)
        if serializerData.is_valid():
            serializerData.save()
            return Response({'msg': 'data updated', 'data': request.data}, status=status.HTTP_200_OK)
        return Response(serializerData.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        id = pk
        studentData = Student.objects.get(pk=id)
        serializerData = StudentSerializer(
            studentData, data=request.data, partial=True)
        if serializerData.is_valid():
            serializerData.save()
            return Response({'msg': 'data updated', 'data': request.data}, status=status.HTTP_200_OK)
        return Response(serializerData.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        id = pk
        studentData = Student.objects.get(pk=id)
        studentData.delete()
        return Response({'msg': 'data deleted'}, status=status.HTTP_200_OK)
