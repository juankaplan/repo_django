from re import template
from django.http import HttpResponse
from django.shortcuts import render
from appcoder.models import Curso
from django.template import loader
# Create your views here.
def curso(request):
    cursos = Curso.objects.all()
    datos = {"cursos": cursos}
    plantilla = loader.get_template("template1.html")
    documento = plantilla.render(datos)
    return HttpResponse(documento)

def alta_curso(request,nombre):
    curso = Curso(nombre = nombre, camada = 324543)
    curso.save()
    texto = f"Se guardo en la base de datos el curso: Nombre: {curso.nombre} Camada: {curso.camada}"
    return HttpResponse(texto)