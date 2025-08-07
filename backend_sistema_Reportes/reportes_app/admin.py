from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Incidencia, Estado, Prioridad, Comentario, Area, PerfilUsuario

##Lógica Inicial
#Registra tus modelos aquí.
admin.site.register(Incidencia)
admin.site.register(Estado)
admin.site.register(Prioridad)
admin.site.register(Comentario)
admin.site.register(Area)
admin.site.register(PerfilUsuario)

# Clase Admin para Incidencia
# class IncidenciaAdmin(admin.ModelAdmin):
#     list_display = ('ticket_unico', 'titulo', 'estado', 'prioridad', 'reportado_por', 'asignado_a', 'fecha_creacion')
#     list_filter = ('estado', 'prioridad', 'fecha_creacion')
#     search_fields = ('titulo', 'descripcion', 'ticket_unico')
#     readonly_fields = ('ticket_unico', 'fecha_creacion')
#
# # Clase Admin para Comentario
# class ComentarioAdmin(admin.ModelAdmin):
#     list_display = ('autor', 'incidencia', 'fecha_creacion')
#     list_filter = ('autor', 'incidencia')
#     search_fields = ('texto',)
#
# # Clase Admin para PerfilUsuario
# class PerfilUsuarioAdmin(admin.ModelAdmin):
#     list_display = ('usuario', 'area')
#     list_filter = ('area',)
#
# # Registra tus modelos con las clases Admin personalizadas
# admin.site.register(Incidencia, IncidenciaAdmin)
# admin.site.register(Estado)
# admin.site.register(Prioridad)
# admin.site.register(Comentario, ComentarioAdmin)
# admin.site.register(Area)
# admin.site.register(PerfilUsuario, PerfilUsuarioAdmin)

