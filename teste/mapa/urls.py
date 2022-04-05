from django.urls import path
from . import views

app_name = 'mapa'

urlpatterns = [
    path('cidade/<int:pk>/', views.CidadesDetailView.as_view(), name='cidade'),
    path('cidades/', views.CidadesLista, name='mapacidades'),
    path('cidades/geo/', views.GeoCidades, name='geojsoncidades'),
    path('paises/geo/', views.GeoPaises, name='geojsonpaises'),
    path('paises/', views.PaisesLista, name='mapapaises')
]