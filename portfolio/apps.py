'''Configura a aplicação 'Portfolio' no Django'''
from django.apps import AppConfig



class PortfolioConfig(AppConfig):
    '''Configuração da aplicação Portfolio'''
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'portfolio'
