from django.db import models
from django.contrib.auth.models import User

MODALIDAD_SESION = [
    ('PRESENCIAL','Presencial'), #LLAVE BD/Lo que se ve en front
    ('ONLINE', 'Online'),
    ('AMBAS', 'Ambas'),
]

TIPO_SESION = [
    ('INDIVIDUAL','Individual'),
    ('GRUPAL','Grupal'),
    ('CUALQUIERA','Cualquiera de las dos'),
]

DEPARTAMENTOS = [
    ('ARQUITECTURA','Arquitectura'), ('FISICA','Fisica'), ('OBRAS CIVILES','Obras Civiles'), ('BIOTECNOLOGIA','Biotecnologia'),
    ('COMERCIAL','Comercial'), ('ELECTRICA','Electrica'), ('ELECTRONICA','Electronica'), ('HUMANISTICO','Humanistico'),
    ('MECANICA','Mecanica'), ('INDUSTRIAS', 'Industrias'), ('DISEÑO','Diseño'), ('INFORMATICA','Informatica'),
    ('DISEÑO','Diseño'), ('QUIMICA','Quimica y Ambiental'), ('MATEMATICAS','Matematicas'), ('DISEÑO','Diseño'),
    ('MINAS','Minas, Metalurgia, Materiales'), ('QUIMICA','Quimica'),
]

TIPO_MURO = [
    ('AYUDAS','Ayudas'),
    ('PRESTAMOS','Prestamos'),
    ('SERVICIOS','Servicios'),
]

class Publicacion(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    tipoMuro = models.CharField(max_length=10, choices=TIPO_MURO)
    contenido = models.TextField(verbose_name='Comentario')
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    modalidad = models.CharField(max_length=10, choices=MODALIDAD_SESION, blank=True, null=True)
    tipoSesion = models.CharField(max_length=15, choices=TIPO_SESION, blank=True, null=True)
    asignatura = models.CharField(max_length=20, choices=DEPARTAMENTOS, blank=True, null=True)
    materialPrestamo = models.CharField(max_length=150, blank=True, null=True)
    cantMaterial = models.PositiveIntegerField(blank=True, null=True)
    titulo = models.CharField(max_length=150, blank=True, null=True)

def __str__(self):
        return f"[{self.get_tipo_muro_display()}] {self.usuario.username}"
