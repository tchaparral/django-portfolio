'''Configura as URLs do Django, incluindo a URL de administração.'''
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('portfolio.urls')),
    path('', include('users.urls'))
]
