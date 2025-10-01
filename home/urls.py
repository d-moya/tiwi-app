from django.urls import path
from . import views

urlpatterns = [
    # Esta ruta DENTRO de la app llama a la vista 'home'
    path('', views.home, name='home'), 
]
