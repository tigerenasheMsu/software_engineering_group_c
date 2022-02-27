from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.register, name='registering'),
    path('status/', views.check_Registration_Status, name='check_registration_status'),
]