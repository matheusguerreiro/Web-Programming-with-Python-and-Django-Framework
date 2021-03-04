from django.contrib import admin

# Register your models here.

from .models import Produto, Cliente

class ProdutoAdimin(admin.ModelAdmin):
    list_display = ('nome', 'preco')

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email')

admin.site.register(Produto, ProdutoAdimin)
admin.site.register(Cliente, ClienteAdmin)