from django.db import models

# Create your models here.

class Produto(models.Model):
    nome = models.CharField('Nome', max_length=43)
    preco = models.DecimalField('Preço', decimal_places=2, max_digits=7)
    estoque = models.IntegerField('Estoque')

class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=21)
    sobrenome = models.CharField('Sobrenome', max_length=32)
    email = models.EmailField('E-mail', max_length=43)

