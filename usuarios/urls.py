from django.urls import path
from . import views

urlpatterns = [
    path('registro/', views.registro_usuario, name='registro'),
    path('perfil/editar/', views.editar_perfil, name='editarPerfil'),
    path('perfil/<str:username>/', views.ver_perfil, name='perfilPublico'),
]