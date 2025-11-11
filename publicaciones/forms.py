from django import forms
from .models import FiltrarPreferencias
from .models import Publicacion
from .models import Comentario

class FormAyudas(forms.ModelForm):
    class Meta:
        model = Publicacion

        fields = [
            'titulo', 'modalidad', 'tipoSesion', 'asignatura', 'contenido','diaPref',
        ]

        labels = {
            'titulo': 'Titulo de la publicacion',
            'modalidad': 'Modalidad de Asistencia',
            'tipoSesion': 'Tipo de Sesion',
            'asignatura': 'Escoge Departamento de Estudio',
            'diaPref': 'Que dias te acomodan mas',
            'contenido': 'Agrega inforacion estra sobre la ayuda que necesitas (importante: dejar dato de contacto)',

        }
        widgets = {
            'titulo': forms.TextInput(attrs={'class':'#'}),
            'modalidad' : forms.Select(attrs={'class':'#'}),
            'tipoSesion' : forms.Select(attrs={'class': '#'}),
            'asignatura' : forms.Select(attrs={'class': '#'}),
            'diaPref' : forms.Select(attrs={'class': '#'}),
            'contenido' : forms.Textarea(attrs={'class': '#'}),
            

        }

class FormTutoria(forms.ModelForm):
    class Meta:
        model = Publicacion

        fields = [
            'titulo','modalidad', 'tipoSesion', 'asignatura', 'contenido', 'diaPref',
        ]

        labels = {
            'titulo': 'itulo de la publicacion',
            'modalidad': 'Modalidad de Asistencia',
            'tipoSesion': 'Tipo de Sesion',
            'asignatura': 'Escoge Departamento de Estudio',
            'diaPref': 'Que dias te acomodan mas',
            'contenido': 'Agrega inforacion estra sobre la ayuda que necesitas (importante: dejar dato de contacto)',

        }

        widgets = {
            'titulo': forms.TextInput(attrs={'class':'#'}),
            'modalidad' : forms.Select(attrs={'class':'#'}),
            'tipoSesion' : forms.Select(attrs={'class': '#'}),
            'asignatura' : forms.Select(attrs={'class': '#'}),
            'diaPref' : forms.Select(attrs={'class': '#'}),
            'contenido' : forms.Textarea(attrs={'class': '#'}),

        }

class FormPrestamos(forms.ModelForm):
    class Meta:
        model = Publicacion

        fields = [
            'materialPrestamo', 'cantMaterial','contenido', 'fotoMaterial',
        ]

        labels = {
            'materialPrestamo': 'Nombre del objeto de prestamo',
            'cantMaterial': 'Cantidad',
            'contenido': 'Agrega inforacion estra sobre la ayuda que necesitas (importante: dejar dato de contacto)',
            'fotoMaterial' : 'Inserta imagen aqui'

        }
        widgets = {
            'materialPrestamo': forms.TextInput(attrs={'class': '#'}),
            'cantMaterial': forms.NumberInput(attrs={'class': '#'}),
            'contenido': forms.Textarea(attrs={'class': '#'}),

        }

class FormComentarios(forms.ModelForm):
    class Meta:
        model = Comentario

        fields = ['contenido']
        labels = {'contenido': ''
                  }
        widgets = {
            'contenido': forms.Textarea(attrs={'rows': 2, 'placeholder': 'Escribe tu comentario','class': '#'})
        }
class EncuestaAyudantia(forms.ModelForm):
    class Meta: 
        model: FiltrarPreferencias

        fields =[
          'modalidad','Comunicacion','metododeestudio','dias','asignatura',
        ]
        labels = {
            "Tiporeunion":"¿De qué forma tu quisieras reunirte en la ayudantia?",
            "Comunicacion":"¿De qué manera te acomoda mas comunicarte con el ayudante?",
            "metododeestudio":"¿Cuál es metodo de estudio te acomoda más?",
            "dias":"¿Que dias te acomodan mas para la ayudantia?",
            "asignatura":"¿Que asignatura te gustaria para la ayudantia?",
        }
        widgets ={
        "Tiporeunion": forms.Select(attrs={'class':'#'}),
        "Comunicacion": forms.Select(attrs={'class':'#'}),
        "metododeestudio": forms.Select(attrs={'class':'#'}),
        "dias": forms.Select(attrs={'class':'#'}),
        "asignatura": forms.Select(attrs={'class':'#'}),
        }
