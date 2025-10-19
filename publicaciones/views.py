from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def muro_prestamos_view(request):

    return render(request, 'publicaciones/muro_base.html', {'muro_nombre': 'Préstamos'})

def muro_ayudas_view(request):

    return render(request, 'publicaciones/muro_base.html', {'muro_nombre': 'Ayudas'})

def muro_servicio_view(request):

    return render(request, 'publicaciones/muro_base.html', {'muro_nombre': 'Servicio'})

@login_required 
def crear_publicacion_view(request):
    return render(request, 'publicaciones/crear_publicacion.html')
