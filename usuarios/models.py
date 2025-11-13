from django.db import models
from django.contrib.auth.models import User
from publicaciones.models import Publicacion

class perfilUsuario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fotoPerfil = models.ImageField(upload_to='usuarios_fotos/', blank=True)
    fechaUnion = models.DateField(auto_now_add=True)
    Carrera = models.CharField(max_length=200, blank=True, null = True)
    Contacto = models.CharField(max_length=400, blank=True, null=True)
