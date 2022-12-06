from django.shortcuts import render
from Appfamily import *
from .models import*
from django.http import HttpResponse

# Create your views here.

def familiar(request):

    mama= Familiar(nombre="migdalia",apellido="Salazar",edad=60,afinidad="mama")
    mama.save()
    cadena_texto=f"Familiar guardado nombre:{mama.nombre}, apellido:{mama.apellido}, edad: {mama.edad}"
    return HttpResponse(cadena_texto)
