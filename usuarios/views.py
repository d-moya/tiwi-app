from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm #
from django.contrib import messages

def registro_usuario(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST) 
        
        if form.is_valid():
            form.save()
            messages.success(request, 'ya puedes iniciar sesión.')
            return redirect('login') 
    
    else:
        form = UserCreationForm()
    return render(request, 'registro.html', {'form': form})