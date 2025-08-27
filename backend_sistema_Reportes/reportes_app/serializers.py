from rest_framework import serializers
from .models import Incidencia, Estado, Prioridad, Area, Comentario
from django.contrib.auth.models import User


# Serializer for the User model, to include only the necessary information
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


# Serializer for the Status model
class EstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estado
        fields = ['id', 'nombre_estado']


# Serializer for the Priority model
class PrioridadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prioridad
        fields = ['id', 'nombre_prioridad']


# Serializer for the Comment model
class ComentarioSerializer(serializers.ModelSerializer):
    # We use the user serializer to show who made the comment
    autor = UserSerializer(read_only=True)

    class Meta:
        model = Comentario
        fields = ['id', 'texto', 'fecha_creacion', 'autor']


# Main serializer for the Incidencia model
class IncidenciaSerializer(serializers.ModelSerializer):
    # The user serializer to show details of the person who reported
    reportado_por = UserSerializer(read_only=True)

    # We use a custom serializer to get the state details
    estado = EstadoSerializer(read_only=True, allow_null=True)

    # This field allows writing the state using its ID, which is common in a POST request
    estado_id = serializers.PrimaryKeyRelatedField(
        queryset=Estado.objects.all(),
        source='estado.nombre_estado',
        write_only=True
    )

    # The priority serializer to show the priority name
    prioridad = PrioridadSerializer(read_only=True)

    class Meta:
        model = Incidencia
        # Fields to be included in the API. We add 'estado_id' for writing
        fields = [
            'id', 'ticket_unico', 'titulo', 'descripcion', 'ubicacion',
            'foto', 'fecha_creacion', 'fecha_resolucion', 'estado',
            'prioridad', 'reportado_por', 'asignado_a', 'estado_id'
        ]
        # Fields that can be read, but cannot be written directly
        read_only_fields = ['ticket_unico', 'fecha_creacion', 'fecha_resolucion', 'reportado_por']

