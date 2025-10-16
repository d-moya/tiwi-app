from django.urls import path
from . import views

urlpatterns = [
    path('', views.crear_publicacion, name='crear_publicacion'),
]