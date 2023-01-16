from django.shortcuts import render
from datetime import datetime
# Create your views here.
def myappHome(request):
    value = 'Rashad'
    language = 'python'
    course = '4 month'
    date = datetime.now()
    stu = {'stu1':{'name':'Habib', 'roll':101}, 'stu2':{'name':'Rayhan', 'roll':102}}
    context = {'lang':language, 'cors':course, 'name':value, 'date':date, 'stu':stu}
    return render(request,'myapp/index.html', context)