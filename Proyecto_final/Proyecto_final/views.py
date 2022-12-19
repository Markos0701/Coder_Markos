from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template import loader



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

"""
def Sitio_web(request):

    diccionario={"nombre":"Markos","apellido":"Mavarez","edad":str(28),"lista_de_notas":[10,9,5,7,8]}

    archivo=open("C:/Users/PC_ITF-QUILMES/Downloads/Curso_Python/git_repos/Proyecto_final/Templates/template1.html")
    template=Template(archivo.read())
    archivo.close()
    contexto=Context(diccionario)
    documento= template.render(contexto)
    
    return HttpResponse(documento)
"""
def Sitio_web(request):

    diccionario={"nombre":"Markos","apellido":"Mavarez","edad":str(28),"lista_de_notas":[10,9,5,7,8]}

    template= loader.get_template("template1.html")
    
    documento= template.render(diccionario)
    
    return HttpResponse(documento)

def Sitio_web2(request):

    teste={"Hola":"Markos"}

    template2= loader.get_template("template2.html")
    
    documento2= template2.render(teste)
    
    return HttpResponse(documento2)