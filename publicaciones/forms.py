from django import forms
from .models import Publicacion

class FormAyudas(forms.ModelForm):
    class Meta:
        model = Publicacion

        fields = [
            'modalidad', 'tipoSesion', 'asignatura', 'contenido'
        ]

        labels = {
            'modalidad': 'Modalidad de Asistencia',
            'tipoSesion': 'Tipo de Sesion',
            'asignatura': 'Escoge Departamento de Estudio',
            'contenido': 'Agrega inforacion estra sobre la ayuda que necesitas (importante: dejar dato de contacto)',

        }
        widgets = {


        }

class FormTutoria(forms.ModelForm):
    class Meta:
        model = Publicacion

        fields = [
            'modalidad', 'tipoSesion', 'asignatura', 'contenido'
        ]

        labels = {
            'modalidad': 'Modalidad de Asistencia',
            'tipoSesion': 'Tipo de Sesion',
            'asignatura': 'Escoge Departamento de Estudio',
            'contenido': 'Agrega inforacion estra sobre la ayuda que necesitas (importante: dejar dato de contacto)',

        }

        widgets = {
            

        }

class FormPrestamos(forms.ModelForm):
    class Meta:
        model = Publicacion

        fields = [
            'materialPrestamo', 'cantMaterial','contenido'
        ]

        labels = {
            'materialPrestamo': 'Nombre del objeto de prestamo',
            'cantMaterial': 'Cantidad',
            'contenido': 'Agrega inforacion estra sobre la ayuda que necesitas (importante: dejar dato de contacto)',

        }
        widgets = {
            

        }