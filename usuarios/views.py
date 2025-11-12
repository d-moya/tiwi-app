from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm 
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import perfilUsuario 
from .forms import PerfilUsuarioForm

def registro_usuario(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST) 
        
        if form.is_valid():
            nuevoUsuario = form.save()
            perfilUsuario.objects.create(usuario=nuevoUsuario)
            messages.success(request, 'ya puedes iniciar sesión.')
            return redirect('login') 
    
    else:
        form = UserCreationForm()
    return render(request, 'registro.html', {'form': form})

@login_required
def perfilusuario(request):
    perfil = get_object_or_404(perfilUsuario, usuario=request.user)
    dicto = {
        'perfilusuario': perfil
    }
    return render(request,'perfil_usuario.html' , dicto)

@login_required
def editarPerfil(request):
    perfil = get_object_or_404(perfilUsuario, usuario=request.user)
    if request.method == 'POST':
        formEP = PerfilUsuarioForm(request.POST, request.FILES, instance=perfil)
        if formEP.is_valid():
            formEP.save()
            messages.success(request, 'Se actualizo su perfil')
            return redirect('perfilUsuario')
    else: 
        formEP = PerfilUsuarioForm(instance=perfil)
        Dicto2 = {'perfil': formEP}
    return render(request,'editar_perfil' , Dicto2)