from django.shortcuts import render
from .models import (
    DatosPersonales, Experiencia, Logro, Curso, 
    ProductoAcademico, ProductoLaboral, Garage
)

def home(request):
    # Obtenemos los datos de cada sección
    # .first() para datos personales porque solo suele haber uno
    perfil = DatosPersonales.objects.first() 
    
    # .all() para las listas de elementos
    experiencias = Experiencia.objects.all()
    logros = Logro.objects.all()
    cursos = Curso.objects.all()
    prod_academicos = ProductoAcademico.objects.all()
    prod_laborales = ProductoLaboral.objects.all()
    articulos_garage = Garage.objects.all()

    # Enviamos todo al HTML dentro de este diccionario
    contexto = {
        'perfil': perfil,
        'experiencias': experiencias,
        'logros': logros,
        'cursos': cursos,
        'prod_academicos': prod_academicos,
        'prod_laborales': prod_laborales,
        'articulos_garage': articulos_garage,
    }
    
    return render(request, 'signup.html', contexto)