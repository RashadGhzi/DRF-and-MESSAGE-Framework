from django.shortcuts import render
from django.contrib import messages

# Create your views here.
def message(request):
    messages.success(request, 'Updated Successfully')
    messages.info(request, 'This is Information')
    messages.warning(request, 'Your are in warning')
    messages.error(request, 'You are in danger')
    return render(request, 'app/index.html')