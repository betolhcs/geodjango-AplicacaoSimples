from pathlib import Path
from django.contrib.gis.utils import LayerMapping
from .models import WorldBorders, Cidade

world_mapping = {
    'fips' : 'FIPS',
    'iso2' : 'ISO2',
    'iso3' : 'ISO3',
    'un' : 'UN',
    'name' : 'NAME',
    'area' : 'AREA',
    'pop2005' : 'POP2005',
    'region' : 'REGION',
    'subregion' : 'SUBREGION',
    'lon' : 'LON',
    'lat' : 'LAT',
    'mpoly' : 'MULTIPOLYGON',
}

cidade_mapping = {
    'nome' : 'NAME',
    'coordenadas' : 'POINT',
}

cidade_shp = Path(__file__).resolve().parent / 'CIDADES' / 'ne_10m_populated_places.shp'
world_shp = Path(__file__).resolve().parent / 'WORLDBORDERS' / 'TM_WORLD_BORDERS-0.3.shp'

def run_world(verbose=True):
    lm = LayerMapping(WorldBorders, world_shp, world_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)

def run_cidade(verbose=True):
    lm = LayerMapping(Cidade, cidade_shp, cidade_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)