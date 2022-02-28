from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse
from voters_registration.models import VotersRegistration
from voters_registration.forms import RegistrationForm


# Create your views here.
def register(request):
    if request.method == "POST":
        firstname = request.POST['firstname']
        surname = request.POST['surname']
        id_number = request.POST['id_number']
        address = request.POST['address']
        date_of_birth = request.POST['date_of_birth']
        print(firstname,surname,id_number,address,date_of_birth)
        ins = VotersRegistration(firstname=firstname,surname=surname,id_number=id_number,address=address,date_of_birth=date_of_birth)
        ins.save()
    return render(request,'voters_registration/registration.html')
    
def check_Registration_Status(request):
    
    id_number_log = request.POST.get('id_number_log', False)
    
    if request.method == "POST":
        if VotersRegistration.objects.filter(id_number=id_number_log).exists():
            print("Logged In")
    return render(request,'voters_registration/status_check.html')