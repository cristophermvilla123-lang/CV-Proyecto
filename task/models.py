from django.db import models

# 1. INICIO (Agregamos cédula para que coincida con tu HTML)
class DatosPersonales(models.Model):
    nombre_completo = models.CharField(max_length=200)
    cedula = models.CharField(max_length=15, default="0000000000") # Campo nuevo solicitado por el HTML
    profesion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    correo = models.EmailField()
    direccion = models.TextField()

    def __str__(self):
        return self.nombre_completo

# 2. EXPERIENCIA (Añadimos descripción para las funciones realizadas)
class Experiencia(models.Model):
    puesto = models.CharField(max_length=200)
    empresa = models.CharField(max_length=200)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(null=True, blank=True)
    actual = models.BooleanField(default=False)
    descripcion = models.TextField(blank=True, null=True) # Para las 'Funciones Realizadas' del HTML

    def __str__(self):
        return f"{self.puesto} en {self.empresa}"

# 3. LOGROS
class Logro(models.Model):
    titulo = models.CharField(max_length=200)
    entidad = models.CharField(max_length=200, default="Institución") # Cambiado para el HTML
    fecha = models.DateField()
    descripcion = models.TextField()

    def __str__(self):
        return self.titulo

# 4. CURSOS (Sincronizado con nombres del HTML)
class Curso(models.Model):
    nombre = models.CharField(max_length=200) # El HTML usa .nombre
    institucion = models.CharField(max_length=200)
    fecha_finalizacion = models.DateField() # El HTML usa .fecha_finalizacion

    def __str__(self):
        return self.nombre

# 5. PRODUCTOS ACADÉMICOS
class ProductoAcademico(models.Model):
    nombre_proyecto = models.CharField(max_length=200) # El HTML usa .nombre_proyecto
    descripcion = models.TextField()
    categoria = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_proyecto

# 6. PRODUCTOS LABORALES
class ProductoLaboral(models.Model):
    nombre_herramienta = models.CharField(max_length=200) # El HTML usa .nombre_herramienta
    logro_clave = models.TextField() # El HTML usa .logro_clave (singular)

    def __str__(self):
        return self.nombre_herramienta

# 7. GARAGE
class Garage(models.Model):
    articulo = models.CharField(max_length=100) # El HTML usa .articulo
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=50)
    publicado_el = models.DateField(auto_now_add=True) # El HTML usa .publicado_el

    def __str__(self):
        return self.articulo