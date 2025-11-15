from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import perfilUsuario 
from .forms import PerfilUsuarioForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from publicaciones.models import Publicacion
import random

FOTOS_DEFECTO = [
    'usuarios_fotos/prede_1.png',
    'usuarios_fotos/prede_2.png',
    'usuarios_fotos/prede_3.png',
]

def registro_usuario(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST) 
        if form.is_valid():
            nuevoUsuario = form.save()
            foto_aleatoria = random.choice(FOTOS_DEFECTO)
            perfilUsuario.objects.create( 
                usuario=nuevoUsuario, 
                fotoPerfil=foto_aleatoria) 
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registro.html', {'form': form})

@login_required
def ver_perfil(request):
    perfil = get_object_or_404(perfilUsuario, usuario=request.user)
    
    contexto = {
        'perfil': perfil,
        'usuario': request.user,
    }
    
    return render(request, 'perfil_usuario.html', contexto)

@login_required
def editar_perfil(request):

    perfil = get_object_or_404(perfilUsuario, usuario=request.user)

    if request.method == 'POST':
        form = PerfilUsuarioForm(request.POST, request.FILES, instance=perfil)
        
        if form.is_valid():
            form.save()
            return redirect('verPerfil') 
    else:
        form = PerfilUsuarioForm(instance=perfil)
    
    contexto = {
        'form': form,
        'perfil': perfil, 
    }
    
    return render(request, 'editar_perfil.html', contexto)

def perfil_publico(request, username):
    # 1. Obtener el objeto User de Django usando el username de la URL
    usuario = get_object_or_404(User, username=username)
    
    # 2. Obtener el objeto perfilUsuario asociado al objeto User
    perfil = get_object_or_404(perfilUsuario, usuario=usuario)
    
    # Opcional: Obtener las publicaciones del usuario (si quieres mostrarlas)
    # publicaciones = Publicacion.objects.filter(autor=usuario).order_by('-fecha_creacion')

    contexto = {
        'perfil': perfil,
        'usuario': usuario, # Es el User que se está viendo
        # 'publicaciones': publicaciones,
    }
    
    # Utiliza la misma plantilla que usas para ver el perfil del usuario logueado o crea una nueva.
    return render(request, 'perfil_usuario.html', contexto)