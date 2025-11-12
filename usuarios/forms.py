from django import forms
from .models import perfilUsuario

class PerfilUsuarioForm(forms.ModelForm):
    class Meta:
        model = perfilUsuario
        fields = ['fotoPerfil', 'Carrera'] 
        widgets = {
            'Carrera': forms.TextInput(attrs={'placeholder': 'Ej. Ingeniería Civil'}),
        }