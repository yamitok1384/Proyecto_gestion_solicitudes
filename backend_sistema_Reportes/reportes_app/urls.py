# urls.py de tu aplicación

from django.urls import path
from .views import login

urlpatterns = [
    path('login/', login, name='login'),
]