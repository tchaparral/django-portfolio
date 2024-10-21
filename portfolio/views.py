'''Módulo para views da portfolio Django.'''
from django.shortcuts import render

def index(request):
    '''Responde à request para a página inicial do portfolio.'''
    return render(request, 'portfolio/index.html')

def politica(request):
    '''Responde à request para a página inicial do portfolio.'''
    return render(request, 'portfolio/politica_de_privacidade.html')
