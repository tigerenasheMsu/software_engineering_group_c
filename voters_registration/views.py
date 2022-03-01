from re import I
from unicodedata import name
from django.shortcuts import render
from .models import VotersRegistration
from django.contrib import messages


# Create your views here.
def register(request):
    if request.method == "POST":
        
        firstname = request.POST['firstname']
        surname = request.POST['surname']
        id_number = request.POST['id_number']
        address = request.POST['address']
        date_of_birth = request.POST['date_of_birth']
        if (VotersRegistration.objects.filter(id_number=id_number).exists()):
            messages.error(request,'The voter you are trying to register, already exists')
        else:
            ins = VotersRegistration(firstname=firstname,surname=surname,id_number=id_number,address=address,date_of_birth=date_of_birth)
            ins.save()
            messages.success(request,'You have been successfuly registered !')
    return render(request,'voters_registration/registration.html')
    
def check_Registration_Status(request):
    
    id_number_log = request.POST.get('id_number_log', False)
    
    if request.method == "POST":
        if VotersRegistration.objects.filter(id_number=id_number_log).exists():
            
            qs = VotersRegistration.objects.filter(id_number=id_number_log)
            
            context = {
            'queryset':qs
            }
            print(id_number_log)
            return render(request,'voters_registration/status_check_result.html',context)
        else:
            messages.error(request,'The National ID you entered does not exist, kindly try again.')
    return render(request,'voters_registration/status_check.html')