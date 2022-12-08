from django.shortcuts import render
from .models import Miembro
from django.http import HttpResponse
from datetime import datetime 


# Create your views here.

def familiar(request):

    familiar_nuevo= Miembro(nombre="kristina", apellido= "Mavarez",edad=32, afinidad= "hermana", fecha_nacimiento= datetime(1990, 7, 1))
    familiar_nuevo.save()
    cadena_texto= f"Familiar Guardado: Nombre: {familiar_nuevo.nombre}  ,__Apellido: {familiar_nuevo.apellido}  ,__Edad: {familiar_nuevo.edad}  ,__afinidad: {familiar_nuevo.afinidad}  ,__fecha: {familiar_nuevo.fecha_nacimiento}"
    return HttpResponse(cadena_texto)