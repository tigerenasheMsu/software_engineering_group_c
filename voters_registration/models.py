from ctypes import addressof
from django.db import models
from datetime import datetime,date

# Create your models here.

class VotersRegistration(models.Model):
    firstname = models.CharField(max_length=15)
    surname = models.CharField(max_length= 15)
    id_number = models.CharField(max_length=13)
    address = models.TextField(max_length=50)
    date_of_birth = models.DateField(auto_now_add=False,auto_now=False,blank=True,null=True)
    timestamp = models.DateField(auto_now_add=True,auto_now=False,blank=True,null=True)
    
class Registration(models.Model):
    firstname = models.CharField(max_length=15)
    surname = models.CharField(max_length= 15)
    id_number = models.CharField(max_length=13)
    address = models.TextField(max_length=50)
    date_of_birth = models.DateField(auto_now_add=False,auto_now=False,blank=True,null=True)
    timestamp = models.DateField(auto_now_add=True,auto_now=False,blank=True,null=True)