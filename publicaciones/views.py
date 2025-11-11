from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import FormAyudas, FormTutoria, FormPrestamos, FormComentarios ,EncuestaAyudantia
from .models import Publicacion, Comentario, FiltrarPreferencias, TIPO_MURO

urlMuros = {
        'AYUDAS': 'muro_ayudas',
        'PRESTAMOS': 'muro_prestamos',
        'SERVICIOS' : 'muro_servicio',
}
    
def validar(request, formulario, tipo_muro_valor, nombreurl, nombreTemplate):
    if request.method == 'POST':
        form = formulario(request.POST, request.FILES) 
        if form.is_valid():
            publicacion = form.save(commit=False)
            publicacion.usuario = request.user 
            publicacion.tipoMuro = tipo_muro_valor 
            publicacion.save()
            return redirect(nombreurl)
    else:
        form = formulario()
    return render(request, nombreTemplate, {'form': form})

@login_required
def home_publicar_view(request):
    return render(request,'publicar/inicio_publicar.html')

def publicar_ayudas_view(request):
    return validar(request,FormAyudas,'AYUDAS', 'muro_ayudas', 'publicar/publicar_ayudas.html')

def publicar_prestamos_view(request):
    return validar(request,FormPrestamos,'PRESTAMOS', 'muro_prestamos', 'publicar/publicar_prestamo.html')

def publicar_tutorias_view(request):
    return validar(request,FormTutoria,'SERVICIOS', 'muro_servicio', 'publicar/publicar_tutoria.html')

def muro_prestamos_view(request):
    publicaciones = Publicacion.objects.filter(tipoMuro = 'PRESTAMOS').order_by('fechaCreacion')
    datitos = {
        'nombre' : 'Prestamos',
        'publicacion' : publicaciones,
        'comentarios' : FormComentarios()
    }
    return render(request, 'Muros/muro_prestamo.html', datitos)

def muro_ayudas_view(request):
    publicaciones = Publicacion.objects.filter(tipoMuro = 'AYUDAS').order_by('-fechaCreacion')
    datitos = {
        'nombre' : 'Ayudas',
        'publicacion' : publicaciones,
        'comentarios' : FormComentarios()
    }
    return render(request, 'Muros/muro_ayudas.html', datitos)

def muro_servicio_view(request):
    publicaciones = Publicacion.objects.filter(tipoMuro = 'SERVICIOS').order_by('-fechaCreacion')
    datitos = {
        'nombre' : 'Servicios',
        'publicacion' : publicaciones,
        'comentarios' : FormComentarios()
    }
    return render(request, 'Muros/muro_tutoria.html', datitos)


@login_required
def comentar(request, publicacion_id, tipo_muro ):
    publicacion = get_object_or_404(Publicacion, id=publicacion_id)
    if request.method == 'POST':
        form = FormComentarios(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.publicacion = publicacion
            comentario.usuario = request.user 
            comentario.save()
        return redirect(urlMuros.get(tipo_muro))
    return redirect(urlMuros.get(tipo_muro))

def eliminarPub(request, publicacion_id):
    publicacion = get_object_or_404(Publicacion, id=publicacion_id)
    muro = publicacion.tipoMuro
    if request.method == 'POST':
        if publicacion.usuario == request.user:
            publicacion.delete()
    urlMuro = urlMuros.get(muro)
    return redirect(urlMuro)
    

def Encuestas(request):
    return render(request,'publicar/Encuesta_ayudantia.html')
@login_required
def preferencias_ayudas_view(request):
    publicaciones_query = FiltrarPreferencias.objects.filter(TIPO_MURO)
    if request.method == 'GET':
    return render(request, 'publicar/Encuesta_ayudantia.html', {'form': form})
    

   