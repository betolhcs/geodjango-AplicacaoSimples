from multiprocessing import context
from textwrap import indent
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.generic import DetailView
from .models import Cidade, WorldBorders
from django.core.serializers import serialize

class CidadesDetailView(DetailView):
    """
        City detail view.
    """
    template_name = 'mapa/cidade-detail.html'
    model = Cidade

def GeoCidades(request):
    output = serialize('geojson', Cidade.objects.all()[:50], indent=2)
    with open("cidades.json", "w") as text_file:
        text_file.write(output)

    return HttpResponse(output, content_type="application/json")

def GeoPaises(request):
    output = serialize('geojson', WorldBorders.objects.all()[:50], indent=2)
    with open("paises.json", "w") as text_file:
        text_file.write(output)

    return HttpResponse(output, content_type="application/json")

def CidadesLista(request):
    return render(request, 'mapa/cidades-lista.html')

def PaisesLista(request):
    return render(request, 'mapa/paises-lista.html')