from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import login, IncidenciaViewSet

# Crea un router y registra nuestro ViewSet
router = DefaultRouter()
router.register(r'incidencias', IncidenciaViewSet)

urlpatterns = [
    # Mantiene la URL de login
    path('login/', login, name='login'),
    # Incluye las URLs generadas por el router para las incidencias
    path('', include(router.urls)),
]
