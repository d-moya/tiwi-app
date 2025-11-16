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

def ver_perfil(request, username):
    usuario = get_object_or_404(User, username=username)
    perfil, created = perfilUsuario.objects.get_or_create(
        usuario=usuario,
        defaults={
            'fotoPerfil': random.choice(FOTOS_DEFECTO),
        }
    )
        
    contexto = {
        'usuario': usuario,
        'perfil': perfil
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
    usuario = get_object_or_404(User, username=username)
 
    perfil = get_object_or_404(perfilUsuario, usuario=usuario)
 
    contexto = {
        'perfil': perfil,
        'usuario': usuario,
    }
    
    return render(request, 'perfil_usuario.html', contexto)