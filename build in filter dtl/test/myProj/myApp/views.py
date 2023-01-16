from django.shortcuts import render

# Create your views here.
def myAppHome(request):
    return render(request, 'myApp/index.html')