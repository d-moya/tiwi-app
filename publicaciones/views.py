from django.shortcuts import render

def crear_publicacion(request):
    return render(request, 'publicar/form_publicacion.html', {})
