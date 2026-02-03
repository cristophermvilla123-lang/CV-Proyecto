from django.shortcuts import render
from .models import (
    DatosPersonales,
    ExperienciaLaboral,
    Reconocimiento,
    CursoRealizado,
    ProductoAcademico,
    ProductoLaboral,
    VentaGarage
)

def home(request):
    # Datos personales (normalmente solo uno)
    perfil = DatosPersonales.objects.first()

    # Listas
    experiencias = ExperienciaLaboral.objects.all()
    logros = Reconocimiento.objects.all()
    cursos = CursoRealizado.objects.all()
    prod_academicos = ProductoAcademico.objects.all()
    prod_laborales = ProductoLaboral.objects.all()
    articulos_garage = VentaGarage.objects.all()

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