from django.shortcuts import render
from drf_app.serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from .models import UserModel
# Create your views here.


class UserView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'drf_app/index.html'

    def get(self, request):
        data = UserSerializer(
            UserModel.objects.all(), many=True).data
        context = {'data': data}
        return render(request, self.template_name, context)
