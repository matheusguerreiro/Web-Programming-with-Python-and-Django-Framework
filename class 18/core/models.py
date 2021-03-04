from django.db import models

# Create your models here.

class Produto(models.Model):
    nome = models.CharField('Nome', max_length=32)
    preco = models.DecimalField('Preço', decimal_places=2, max_digits=7)
    estoque = models.IntegerField('Estoque')

    def __str__(self):
        return self.nome


class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=43)
    email = models.EmailField('E-mail', max_length=43)

    def __str__(self):
        return self.nome
