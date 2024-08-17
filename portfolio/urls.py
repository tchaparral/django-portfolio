'''Define as rotas de URL para a aplicação Portfolio'''
from django.urls import path
from portfolio.views import index

urlpatterns = [
    path('', index, name='index')
]
