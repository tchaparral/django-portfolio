'''Define as rotas de URL para a aplicação Portfolio'''
from django.urls import path
from portfolio.views import index, politica

urlpatterns = [
    path('', index, name='index'),
    path('politica-de-privacidade', politica, name='politica')
]
