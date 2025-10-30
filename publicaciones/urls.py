from django.urls import path
from . import views

urlpatterns = [
    path('muros/prestamos/', views.muro_prestamos_view, name='muro_prestamos'),
    path('muros/ayudas/', views.muro_ayudas_view, name='muro_ayudas'),
    path('muros/servicio/', views.muro_servicio_view, name='muro_servicio'),
    path('publicar/home', views.home_publicar_view, name='home_publicar'),
    path('formulario/ayudas', views.publicar_ayudas_view, name='form_ayudas'),
    path('formulario/prestamos', views.publicar_prestamos_view, name='form_prestamo'),
    path('formulario/servicio', views.publicar_tutorias_view, name='form_tutoria'),
    path('Encuesta/ayudas', views.publicar_ayudas_view, name='preferencias_ayudas'),
    path('Encuesta/prestamos', views.publicar_prestamos_view, name='preferencias_prestamo'),
    path('Encuesta/servicio', views.publicar_tutorias_view, name='preferencias_tutoria'),
]