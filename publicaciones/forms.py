from django import forms
from .models import FiltrarPreferencias
from .models import Publicacion
from .models import Comentario

class FormAyudas(forms.ModelForm):
    class Meta:
        model = Publicacion

        fields = [
            'titulo', 'modalidad', 'tipoSesion', 'asignatura','dias','Comunicacion', 'contenido','metododeestudio',
        ]

        labels = {
            'titulo': 'Titulo de la publicacion',
            'modalidad': 'Modalidad de Asistencia',
            'tipoSesion': 'Tipo de Sesion',
            'asignatura': 'Escoge Departamento de Estudio',
            'diaPref': 'Que dias te acomodan mas',
            "Comunicacion":"¿De qué manera te acomoda mas comunicarte con el ayudante?",
            "metododeestudio":"¿Cuál es metodo de estudio te acomoda más?",
            'contenido': 'Agrega inforacion estra sobre la ayuda que necesitas (importante: dejar dato de contacto)',


        }
        widgets = {
            'titulo': forms.TextInput(attrs={'class': '#'}),
            'modalidad' : forms.Select(attrs={'class': '#'}),
            'tipoSesion' : forms.Select(attrs={'class': '#'}),
            'asignatura' : forms.Select(attrs={'class': '#'}),
            'dias' : forms.Select(attrs={'class': '#'}),
            'contenido' : forms.Textarea(attrs={'class': '#'}),
            

        }

class FormTutoria(forms.ModelForm):
    class Meta:
        model = Publicacion

        fields = [
            'titulo', 'modalidad', 'tipoSesion', 'asignatura','dias','Comunicacion', 'contenido','metododeestudio',
        ]

        labels = {
            'titulo': 'itulo de la publicacion',
            'modalidad': 'Modalidad de Asistencia',
            'tipoSesion': 'Tipo de Sesion',
            'asignatura': 'Escoge Departamento de Estudio',
            'dias': 'Que dias te acomodan mas',
            'contenido': 'Agrega inforacion estra sobre la ayuda que necesitas (importante: dejar dato de contacto)',
            "Comunicacion":"¿De qué manera te acomoda mas comunicarte con el ayudante?",
            "metododeestudio":"¿Cuál es metodo de estudio te acomoda más?",

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
        model= FiltrarPreferencias

        fields =[
          'modalidad','Comunicacion','metododeestudio','dias','asignatura', 'tipoSesion',
        ]

        labels = {
            "modalidad":"¿De qué manera te sería más cómodo reunirte en una ayudantía?",
            "Comunicacion":"¿Por cuál medio te acomodaría más comunicarte con otros usuarios?",
            "metododeestudio":"¿Cuál/es de estos métodos de estudio te acomodan más?",
            "dias":"¿En qué días tienes más tiempo libre para estudiar cómodamente?",
            "asignatura":"¿Cuál asignatura es de tu mayor interés en este momento?",
            "tipoSesion": "¿Te sentirías más cómodo en una sesión individual (sólo el tutor y el alumno) o junto a más personas?",
        }
        widgets ={
        "modalidad": forms.Select(attrs={'class':'#'}),
        "Comunicacion": forms.Select(attrs={'class':'#'}),
        "metododeestudio": forms.Select(attrs={'class':'#'}),
        "dias": forms.Select(attrs={'class':'#'}),
        "asignatura": forms.Select(attrs={'class':'#'}),
        'tipoSesion': forms.Select(attrs={'class':'#'}),
        }
