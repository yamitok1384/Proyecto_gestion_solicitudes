from django.db import models

# Modelo usuario

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import uuid  # Importamos la librería uuid para generar el ticket único

# Modelos para campos de selección (ej. estado y prioridad)
class Estado(models.Model):
    nombre_estado = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_estado

class Prioridad(models.Model):
    nombre_prioridad = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_prioridad

class Area(models.Model):
    nombre_area = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_area

# Modelo para extender la información del usuario de Django
class PerfilUsuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    area = models.ForeignKey(Area, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.usuario.username

# Función para crear automáticamente el perfil de usuario
@receiver(post_save, sender=User)
def crear_o_actualizar_perfil_de_usuario(sender, instance, created, **kwargs):
    if created:
        PerfilUsuario.objects.create(usuario=instance)
    instance.perfilusuario.save()


 ### lógica inicial pero no generaba el numero de ticket unico por defecto
class Incidencia(models.Model):
    ticket_unico = models.CharField(max_length=100, unique=True, blank=True)
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    ubicacion = models.CharField(max_length=255)
    foto = models.ImageField(upload_to='incidencias/', null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_resolucion = models.DateTimeField(null=True, blank=True)

    # Relaciones (Foreign Keys)
    estado = models.ForeignKey(Estado, on_delete=models.SET_NULL, null=True)
    prioridad = models.ForeignKey(Prioridad, on_delete=models.SET_NULL, null=True)
    reportado_por = models.ForeignKey(User, on_delete=models.CASCADE, related_name='incidencias_reportadas')
    asignado_a = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='incidencias_asignadas', null=True, blank=True)

    def __str__(self):
        return self.titulo

# Modelo principal para las incidencias (reportes)
# Esta lógica genera el numero de tickets
# Importamos la librería uuid para generar identificadores únicos.
# El método save() se ejecuta cada vez que se guarda una instancia de Incidencia.
# La línea if not self.ticket_unico: comprueba si el campo está vacío.
# Si está vacío, genera un código único de 8 caracteres y se lo asigna.
# La línea super().save(*args, **kwargs) es crucial, ya que llama al método original para que se guarden todos los demás campos.
# class Incidencia(models.Model):
#     # Modelo principal para las incidencias (reportes)
#     class Incidencia(models.Model):
#         ticket_unico = models.CharField(max_length=100, unique=True, blank=True, null=True)
#         titulo = models.CharField(max_length=255)
#         descripcion = models.TextField()
#         ubicacion = models.CharField(max_length=255)
#         foto = models.ImageField(upload_to='incidencias/', null=True, blank=True)
#         fecha_creacion = models.DateTimeField(auto_now_add=True)
#         fecha_resolucion = models.DateTimeField(null=True, blank=True)
#
#         # Relaciones (Foreign Keys)
#         estado = models.ForeignKey(Estado, on_delete=models.SET_NULL, null=True)
#         prioridad = models.ForeignKey(Prioridad, on_delete=models.SET_NULL, null=True)
#         reportado_por = models.ForeignKey(User, on_delete=models.CASCADE, related_name='incidencias_reportadas')
#         asignado_a = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='incidencias_asignadas', null=True,
#                                        blank=True)
#
#         def save(self, *args, **kwargs):
#             # Genera el ticket_unico si es la primera vez que se guarda (el campo está vacío)
#             if not self.ticket_unico:
#                 self.ticket_unico = str(uuid.uuid4())[:8].upper()  # Genera un código único
#             super().save(*args, **kwargs)  # Llama al método original de guardado
#
#         def __str__(self):
#             return self.titulo




# Modelo para los comentarios en las incidencias
class Comentario(models.Model):
    texto = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    # Relaciones
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    incidencia = models.ForeignKey(Incidencia, on_delete=models.CASCADE)

    def __str__(self):
        return f"Comentario de {self.autor.username} en {self.incidencia.titulo}"