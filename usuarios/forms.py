from django import forms
from .models import perfilUsuario

class PerfilUsuarioForm(forms.ModelForm):
    class Meta:
        model = perfilUsuario
        fields = ['fotoPerfil', 'Carrera','Contacto'] 
        labels = {
            'fotoPerfil': '',
            'Carrera': 'Soy de: ',
            'Contacto': 'Comunicate a: '
        }
        widgets = {
            'Carrera': forms.TextInput(),
            'fotoPerfil': forms.FileInput(),
            'Contacto': forms.TextInput(),
        }