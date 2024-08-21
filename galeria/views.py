from django.shortcuts import render
from django.http import HttpResponse #Responsável pelas respostas de requisição

# Create your views here.

""" PARA RENDERIZAR HTML DIRETO DO HTTPRESPONDE
def index(request):
    return HttpResponse('<h1>Alura Space</h1><p>Bem vindo ao espaço</p>')
"""

def index(request):
    return render(request, 'galeria/index.html')