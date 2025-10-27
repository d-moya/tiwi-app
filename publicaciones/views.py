from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def muro_prestamos_view(request):
    return render(request, 'Muros/muro_prestamo.html')

def muro_ayudas_view(request):
    return render(request, 'Muros/muro_ayudas.html')

def muro_servicio_view(request):
    return render(request, 'Muros/muro_tutorias.html')

@login_required
def home_publicar_view(request):
    return render(request,'publicar/inicio_publicar.html')

def publicar_ayudas_view(request):
    return render(request,'publicar/publicar_ayudas.html')

def publicar_prestamos_view(request):
    return render(request,'publicar/publicar_prestamo.html')

def publicar_tutorias_view(request):
    return render(request,'publicar/publicar_tutoria.html')
