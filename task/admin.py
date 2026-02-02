from django.contrib import admin
from .models import (
    DatosPersonales, Experiencia, Logro, Curso, 
    ProductoAcademico, ProductoLaboral, Garage
)

@admin.register(Experiencia)
class ExperienciaAdmin(admin.ModelAdmin):
    def get_readonly_fields(self, request, obj=None):
        if obj: return ('fecha_inicio', 'fecha_fin')
        return []

@admin.register(Logro)
class LogroAdmin(admin.ModelAdmin):
    def get_readonly_fields(self, request, obj=None):
        if obj: return ('fecha',)
        return []

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    def get_readonly_fields(self, request, obj=None):
        if obj: return ('fecha_logro',)
        return []

# Registros estándar para el resto
admin.site.register(DatosPersonales)
admin.site.register(ProductoAcademico)
admin.site.register(ProductoLaboral)
admin.site.register(Garage)