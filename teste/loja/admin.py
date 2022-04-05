from multiprocessing.connection import Client
from django.contrib import admin
from .models import Pedido#, Cliente
# Register your models here.

admin.site.register(Pedido)
# admin.site.register(Cliente)