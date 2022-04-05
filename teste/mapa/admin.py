from django.contrib.gis import admin
from .models import Cidade, WorldBorders

admin.site.register(WorldBorders, admin.ModelAdmin)
admin.site.register(Cidade)


# Register your models here.
