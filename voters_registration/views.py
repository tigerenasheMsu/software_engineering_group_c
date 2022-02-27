from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def register(request):
    return render(request,'voters_registration/registration.html')
    
def check_Registration_Status(request):
    return render(request,'voters_registration/status_check.html')