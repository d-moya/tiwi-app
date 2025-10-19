from django.urls import path
from . import views

urlpatterns = [
    path('muros/prestamos/', views.muro_prestamos_view, name='muro_prestamos'),
    path('muros/ayudas/', views.muro_ayudas_view, name='muro_ayudas'),
    path('muros/servicio/', views.muro_servicio_view, name='muro_servicio'),
    path('publicar/', views.crear_publicacion_view, name='crear_publicacion'),
]