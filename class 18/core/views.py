from django.shortcuts import render
from .models import Produto

# Create your views here.

def index(request):
    produtos = Produto.objects.all()
    contexto = {
        'curso': 'Programação Web com Django Framework.',
        'produtos': produtos
    }
    return render(request, 'index.html', contexto)

def contato(request):
    return render(request, 'contato.html')

def produto(request, pk):
    produtoID = Produto.objects.get(id=pk)
    contexto = {
        'produto': produtoID
    }
    return render(request, 'produto.html', contexto)
