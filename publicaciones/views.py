from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import FormAyudas, FormTutoria, FormPrestamos 

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
    return validar(request,FormAyudas,'AYUDAS', 'muro_ayudas', 'publicar/Encuesta_ayudantia.html')

def publicar_prestamos_view(request):
    return validar(request,FormPrestamos,'PRESTAMOS', 'muro_prestamo', 'publicar/Encuesta_prestamo.html')

def publicar_tutorias_view(request):
    return validar(request,FormTutoria,'SERVICIOS', 'muro_tutoria', 'publicar/Encuesta_tutoria.html')

def muro_prestamos_view(request):
    return render(request, 'Muros/muro_prestamo.html', {'muro_nombre': 'Préstamos'})

def muro_ayudas_view(request):
    return render(request, 'Muros/muro_ayudas.html', {'muro_nombre': 'Ayudas'})

def muro_servicio_view(request):
    return render(request, 'Muros/muro_tutoria.html', {'muro_nombre': 'Servicio'})