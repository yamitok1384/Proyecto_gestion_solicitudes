from rest_framework import serializers
from .models import Incidencia, Estado, Prioridad, Area, Comentario
from django.contrib.auth.models import User


# Serializador para el modelo de usuario, para incluir solo la información necesaria
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


# Serializador para el modelo de Estado
class EstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estado
        fields = ['id', 'nombre_estado']


# Serializador para el modelo de Prioridad
class PrioridadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prioridad
        fields = ['id', 'nombre_prioridad']


# Serializador para el modelo de Comentario
class ComentarioSerializer(serializers.ModelSerializer):
    # Usamos el serializador de usuario para mostrar quién hizo el comentario
    autor = UserSerializer(read_only=True)

    class Meta:
        model = Comentario
        fields = ['id', 'texto', 'fecha_creacion', 'autor']


# Serializador principal para el modelo Incidencia
class IncidenciaSerializer(serializers.ModelSerializer):
    # El serializador del usuario para mostrar los detalles de la persona que reportó
    reportado_por = UserSerializer(read_only=True)

    # El serializador del estado para mostrar el nombre del estado en lugar del ID
    estado = EstadoSerializer(read_only=True)

    # El serializador de prioridad para mostrar el nombre de la prioridad
    prioridad = PrioridadSerializer(read_only=True)

    class Meta:
        model = Incidencia
        # Los campos que se incluirán en la API
        fields = [
            'id', 'ticket_unico', 'titulo', 'descripcion', 'ubicacion',
            'foto', 'fecha_creacion', 'fecha_resolucion', 'estado',
            'prioridad', 'reportado_por', 'asignado_a'
        ]
        # Campos que se pueden leer, pero no se pueden escribir directamente
        read_only_fields = ['ticket_unico', 'fecha_creacion', 'fecha_resolucion', 'reportado_por']


