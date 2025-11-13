from django.urls import path
from . import views

urlpatterns = [
    path('registro/', views.registro_usuario, name='registro'),
    path('perfil/', views.ver_perfil, name='verPerfil'),
    path('perfil/editar/', views.editar_perfil, name='editarPerfil'),
]