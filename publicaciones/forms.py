from django import forms
from .models import Publicacion

class FormAyudas(forms.ModelForm):
    class Meta:
        model = Publicacion

        fields = [
            'titulo', 'modalidad', 'tipoSesion', 'asignatura', 'contenido'
        ]

        labels = {
            'titulo': 'Titulo de la publicacion',
            'modalidad': 'Modalidad de Asistencia',
            'tipoSesion': 'Tipo de Sesion',
            'asignatura': 'Escoge Departamento de Estudio',
            'contenido': 'Agrega inforacion estra sobre la ayuda que necesitas (importante: dejar dato de contacto)',

        }
        widgets = {
            'titulo': forms.TextInput(attrs={'class':'#'}),
            'modalidad' : forms.Select(attrs={'class':'#'}),
            'tipoSesion' : forms.Select(attrs={'class': '#'}),
            'asignatura' : forms.Select(attrs={'class': '#'}),
            'contenido' : forms.Textarea(attrs={'class': '#'}),
            

        }

class FormTutoria(forms.ModelForm):
    class Meta:
        model = Publicacion

        fields = [
            'titulo','modalidad', 'tipoSesion', 'asignatura', 'contenido',
        ]

        labels = {
            'titulo': 'itulo de la publicacion',
            'modalidad': 'Modalidad de Asistencia',
            'tipoSesion': 'Tipo de Sesion',
            'asignatura': 'Escoge Departamento de Estudio',
            'contenido': 'Agrega inforacion estra sobre la ayuda que necesitas (importante: dejar dato de contacto)',

        }

        widgets = {
            'titulo': forms.TextInput(attrs={'class':'#'}),
            'modalidad' : forms.Select(attrs={'class':'#'}),
            'tipoSesion' : forms.Select(attrs={'class': '#'}),
            'asignatura' : forms.Select(attrs={'class': '#'}),
            'contenido' : forms.Textarea(attrs={'class': '#'}),

        }

class FormPrestamos(forms.ModelForm):
    class Meta:
        model = Publicacion

        fields = [
            'titulo','materialPrestamo', 'cantMaterial','contenido',
        ]

        labels = {
            'titulo': 'Titulo de la publicacion',
            'materialPrestamo': 'Nombre del objeto de prestamo',
            'cantMaterial': 'Cantidad',
            'contenido': 'Agrega inforacion estra sobre la ayuda que necesitas (importante: dejar dato de contacto)',

        }
        widgets = {
            'titulo': forms.TextInput(attrs={'class': '#'}),
            'materialPrestamo': forms.TextInput(attrs={'class': '#'}),
            'cantMaterial': forms.NumberInput(attrs={'class': '#'}),
            'contenido': forms.Textarea(attrs={'class': '#'}),

        }