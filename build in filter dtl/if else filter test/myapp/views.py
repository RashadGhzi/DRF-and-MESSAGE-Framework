from django.shortcuts import render
from datetime import datetime
# Create your views here.
def myappHome(request):
    date = datetime.now()
    context = {'date':date, 'val':False, 'nm':'Django', 'st':5}
    return render(request,'myapp/index.html', context)