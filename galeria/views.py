from django.shortcuts import render
from django.http import HttpResponse #Responsável pelas respostas de requisição

# Create your views here.

def index(request):
    return HttpResponse('<h1>Alura Space</h1><p>Bem vindo ao espaço</p>')