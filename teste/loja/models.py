from django.db import models

# Create your models here.

# class Cliente(models.Model):
#     nome = models.CharField(max_length=50)
#     endereco = models.CharField(max_length=50)
#     cep = models.CharField(max_length=10)

class Pedido(models.Model):
    produto = models.CharField(max_length=8)
    quantidade = models.DecimalField(max_digits=8, decimal_places=2)
    data_pedido = models.DateField(auto_now=False, auto_now_add=False)
    cliente_nome = models.CharField(max_length=50)
    cliente_endereco = models.CharField(max_length=50)
    cliente_cep = models.CharField(max_length=10)
    # cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)

    # def __str__(self):
    #     self.produto