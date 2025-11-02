from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import FormAyudas, FormTutoria, FormPrestamos
from .models import Publicacion

def validar(request, form_class, tipo_muro_valor, redirect_name, template_name):
    if request.method == 'POST':
        form = form_class(request.POST) 
        if form.is_valid():
            publicacion = form.save(commit=False)
            publicacion.usuario = request.user 
            publicacion.tipoMuro = tipo_muro_valor 
            publicacion.save()
            return redirect(redirect_name)
    else:
        form = form_class()
    return render(request, template_name, {'form': form})

@login_required
def home_publicar_view(request):
    return render(request,'publicar/inicio_publicar.html')

def publicar_ayudas_view(request):
    return validar(request,FormAyudas,'AYUDAS', 'muro_ayudas', 'publicar/publicar_ayudas.hmtl')

def publicar_prestamos_view(request):
    return validar(request,FormPrestamos,'PRESTAMOS', 'muro_prestamo', 'publicar/publicar_prestamos.html')

def publicar_tutorias_view(request):
    return validar(request,FormTutoria,'SERVICIOS', 'muro_tutoria', 'publicar/publicar_tutoria.html')

def muro_prestamos_view(request):
    publicaciones = Publicacion.objects.filter(tipoMuro = 'PRESTAMOS').order_by('fechaCreacion')
    datitos = {
        'nombre' : 'Prestamos',
        'publicacion' : publicaciones,
    }
    return render(request, 'Muros/muro_prestamo.html', datitos)

def muro_ayudas_view(request):
    publicaciones = Publicacion.objects.filter(tipoMuro = 'AYUDAS').order_by('fechaCreacion')
    datitos = {
        'nombre' : 'Ayudas',
        'publicacion' : publicaciones,
    }
    return render(request, 'Muros/muro_ayudas.html', datitos)

def muro_servicio_view(request):
    publicaciones = Publicacion.objects.filter(tipoMuro = 'SERVICIOS').order_by('-fechaCreacion')
    datitos = {
        'nombre' : 'Servicios',
        'publicacion' : publicaciones,
    }
    return render(request, 'Muros/muro_tutoria.html', datitos)

