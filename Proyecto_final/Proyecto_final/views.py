from django.http import HttpResponse
import datetime


def saludar(request):
    return HttpResponse("hola mundo!")

def segunda_vista(request):
    return HttpResponse ("Ya entendi esto parece ser muy simple")

def dia_de_hoy(request):
    dia= datetime.datetime.today()
    cadena=f"hos es {dia}"
    return HttpResponse(f"hoy es {cadena}")

def saludo_con_nombre(request,nombre):
    return HttpResponse(f"Hola {nombre} como estas?")

def calcula_anio_nacimiento(request,edad):
    anio_actual= datetime.datetime.today().year
    anio_nacimiento= anio_actual - int(edad)
    return HttpResponse(f"<h1> Usted nacio en el año{anio_nacimiento}<h1>")


