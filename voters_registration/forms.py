from pyexpat import model
from attr import fields
from django.forms import ModelForm
from voters_registration.models import Registration

class RegistrationForm(ModelForm):
    class Meta:
        model = Registration
        fields = ['firstname','surname','id_number','address','date_of_birth']