

from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from .models import Incidencia, Estado, Prioridad, Comentario
from .serializers import IncidenciaSerializer
from django.utils import timezone  # Importa timezone para obtener la fecha y hora actuales


# Esta vista maneja el login del usuario
@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    """
    Handles user login. It authenticates the user and returns an
    authentication token if the credentials are valid.
    """
    # Get the username and password from the request data
    username = request.data.get('username')
    password = request.data.get('password')

    # Authenticate the user against the Django database
    user = authenticate(request, username=username, password=password)

    if user is not None:
        # If the user is authenticated, get or create a new token
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})
    else:
        # If authentication fails, return a 401 Unauthorized error
        return Response({'error': 'Invalid credentials'}, status=401)


# Este ViewSet proporciona las operaciones CRUD para el modelo Incidencia
class IncidenciaViewSet(viewsets.ModelViewSet):
    """
    ViewSet que proporciona las operaciones CRUD (Crear, Leer, Actualizar, Eliminar)
    para el modelo Incidencia.
    """
    # Define qué objetos de la base de datos se pueden ver
    queryset = Incidencia.objects.all()

    # Define el serializador a usar para convertir los datos
    serializer_class = IncidenciaSerializer

    # Asegura que el usuario esté autenticado para acceder a las vistas
    permission_classes = [IsAuthenticated]

    # Sobreescribe el método perform_create para asignar automáticamente
    # el usuario que ha iniciado sesión al campo 'reportado_por'
    def perform_create(self, serializer):
        # Genera un ticket único basado en la fecha y hora actuales
        timestamp = timezone.now().strftime('%Y%m%d%H%M%S%f')
        ticket_unico = f"INC-{timestamp}"

        # Guarda la instancia con el usuario y el ticket único
        serializer.save(reportado_por=self.request.user, ticket_unico=ticket_unico)

        #serializer.save(reportado_por=self.request.user)

