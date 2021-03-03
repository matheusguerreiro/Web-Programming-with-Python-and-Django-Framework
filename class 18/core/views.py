from django.shortcuts import render

# Create your views here.

def index(request):
    contexto = {
        'curso': 'Programação Web com Django Framework.'
    }
    return render(request, 'index.html', contexto)

def contato(request):
    return render(request, 'contato.html')