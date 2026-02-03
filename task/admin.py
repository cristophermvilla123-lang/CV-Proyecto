from django.contrib import admin
from .models import (
    Task,
    DatosPersonales,
    ExperienciaLaboral,
    Reconocimiento,
    CursoRealizado,
    ProductoAcademico,
    ProductoLaboral,
    VentaGarage,
    ConfigSeccionesCV
)

# ----------------------------
# TASKS
# ----------------------------
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'important', 'created')
    list_filter = ('important',)
    search_fields = ('title',)


# ----------------------------
# DATOS PERSONALES
# ----------------------------
@admin.register(DatosPersonales)
class DatosPersonalesAdmin(admin.ModelAdmin):
    list_display = ('nombres', 'apellidos', 'numerocedula', 'perfilactivo')
    search_fields = ('nombres', 'apellidos', 'numerocedula')
    list_filter = ('perfilactivo', 'sexo')


# ----------------------------
# EXPERIENCIA LABORAL
# ----------------------------
@admin.register(ExperienciaLaboral)
class ExperienciaLaboralAdmin(admin.ModelAdmin):
    list_display = (
        'cargodesempenado',
        'nombrempresa',
        'fechainiciogestion',
        'fechafingestion',
        'activarparaqueseveaenfront'
    )
    list_filter = ('activarparaqueseveaenfront',)
    search_fields = ('cargodesempenado', 'nombrempresa')

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ('fechainiciogestion',)
        return []


# ----------------------------
# RECONOCIMIENTOS
# ----------------------------
@admin.register(Reconocimiento)
class ReconocimientoAdmin(admin.ModelAdmin):
    list_display = (
        'tiporeconocimiento',
        'fechareconocimiento',
        'entidadpatrocinadora',
        'activarparaqueseveaenfront'
    )
    list_filter = ('tiporeconocimiento', 'activarparaqueseveaenfront')

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ('fechareconocimiento',)
        return []


# ----------------------------
# CURSOS
# ----------------------------
@admin.register(CursoRealizado)
class CursoRealizadoAdmin(admin.ModelAdmin):
    list_display = (
        'nombrecurso',
        'fechainicio',
        'fechafin',
        'totalhoras',
        'activarparaqueseveaenfront'
    )
    list_filter = ('activarparaqueseveaenfront',)

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ('fechainicio', 'fechafin')
        return []


# ----------------------------
# PRODUCTOS ACADÉMICOS
# ----------------------------
@admin.register(ProductoAcademico)
class ProductoAcademicoAdmin(admin.ModelAdmin):
    list_display = ('nombrerecurso', 'clasificador', 'activarparaqueseveaenfront')


# ----------------------------
# PRODUCTOS LABORALES
# ----------------------------
@admin.register(ProductoLaboral)
class ProductoLaboralAdmin(admin.ModelAdmin):
    list_display = ('nombreproducto', 'fechaproducto', 'activarparaqueseveaenfront')


# ----------------------------
# VENTA GARAGE
# ----------------------------
@admin.register(VentaGarage)
class VentaGarageAdmin(admin.ModelAdmin):
    list_display = (
        'nombreproducto',
        'estadoproducto',
        'valordelbien',
        'fechapublicacion',
        'activarparaqueseveaenfront'
    )
    list_filter = ('estadoproducto', 'activarparaqueseveaenfront')


# ----------------------------
# CONFIGURACIÓN CV
# ----------------------------
@admin.register(ConfigSeccionesCV)
class ConfigSeccionesCVAdmin(admin.ModelAdmin):
    list_display = (
        'mostrar_datos_personales',
        'mostrar_experiencia',
        'mostrar_reconocimientos',
        'mostrar_cursos',
        'mostrar_productos_academicos',
        'mostrar_productos_laborales',
        'mostrar_venta_garage',
        'actualizado'
    )


# ----------------------------
# PERSONALIZACIÓN DEL ADMIN
# ----------------------------
admin.site.site_header = "Panel de Administración"
admin.site.site_title = "Administración del CV"
admin.site.index_title = "Gestión de Información del CV"