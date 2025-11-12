from django.urls import path
from . import views

urlpatterns = [
    path('registro/', views.registro_usuario, name='registro'),
    path('perfil/', views.perfilusuario, name='perfilUsuario'),
    path('perfil/editar/', views.editarPerfil, name='editarPerfil'),
]