from django.shortcuts import render

# Create your views here.
# urls.py principal
#
# from django.contrib import admin
# from django.urls import path, include
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/', include('reportes_app.urls')), # <-- Esto incluye las URLs de tu app
# ]

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

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




