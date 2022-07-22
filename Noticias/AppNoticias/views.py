from django.shortcuts import render
from .models import Plantas, Categoria, Servicios, Galeria

# Create your views here.

def home(request):
    primer_noticia=Plantas.objects.first()
    tres_noticia=Plantas.objects.all()[1:3]
    tres_categoria=Categoria.objects.all()[0:3]


    return render (request, 'home.html', {
        'primer_noticia': primer_noticia,
        'tres_noticia': tres_noticia,
        'tres_categoria': tres_categoria,

    })

def categoria(request,):
    categorias=Categoria.objects.all()

    return render (request, 'categorias.html',{
        'categorias': categorias
    })

def servicios(request, ):
    servicios=Servicios.objects.all()

    return render (request, 'servicios.html',{
        'servicios': servicios
    })


def toda_categoria(request, id):

    categorias=Categoria.objects.get(id=id)
    noticia = Plantas.objects.filter(categoria=categorias)

    return render (request, 'toda_categoria.html',{
        'todas_noticias': noticia,
        'categoria': categorias

    })

def todas_noticias(request):
    todas_noticias=Plantas.objects.all()

    return render (request, 'todas_noticias.html', {
        'todas_noticias': todas_noticias
    })

def plantas(request, id):

    noticia=Plantas.objects.get(pk=id)
    categoria=Categoria.objects.get(id=noticia.categoria.id)
    noticia_relacionada=Plantas.objects.filter(categoria=categoria).exclude(id=id)

    return render (request, 'detalles.html', {
        'noticia': noticia,
        'noticia_relacionada': noticia_relacionada,

    })

def detalleServicio(request, id):
    servicios=Servicios.objects.get(pk=id)

    servicioRelacionado=Servicios.objects.all().exclude(id=id)

    return render (request, 'detalleServicio.html',{
        'servicios': servicios,
        'servicioRelacionado': servicioRelacionado,
    })

def contacto(request):

    return render (request, 'contacto.html')

def galeria(request,):
    imagenes= Galeria.objects.all()
    return render (request, 'galeria.html',{
        'imagenes':imagenes
    })