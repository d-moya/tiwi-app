from django.db import models
from django.contrib.auth.models import User
from .models import Publicacion

class perfilUsuario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fotoPerfil = models.ImageField()
    fechaUnion = models.DateField()
