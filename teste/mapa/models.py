from django.contrib.gis.db import models

# Create your models here.
class WorldBorders(models.Model):
    name = models.CharField(max_length=50)
    area = models.IntegerField()
    pop2005 = models.IntegerField('Population 2005')
    fips = models.CharField('FIPS Code', max_length=2, null=True)
    iso2 = models.CharField('2 Digit ISO', max_length=2)
    iso3 = models.CharField('3 Digit ISO', max_length=3)
    un = models.IntegerField('United Nations Code')
    region = models.IntegerField('Region Code')
    subregion = models.IntegerField('Sub-Region Code')
    lon = models.FloatField()
    lat = models.FloatField()

    mpoly = models.MultiPolygonField()

    def __str__(self):
        return self.name

class Cidade(models.Model):
    nome = models.CharField(max_length=100, blank=False)
    coordenadas = models.PointField()

    def __str__(self):
        return self.nome

    class Meta:
        # order of drop-down list items
        ordering = ('nome',)

        # plural form in admin view
        verbose_name_plural = 'cidades'