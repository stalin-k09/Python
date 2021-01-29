"""webinicial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views as core_views

#from distribuidores import views as distribuidores_views

from medicamentos import views as medicamentos_views

from . import settings 

urlpatterns = [
    path('', core_views.home, name="home"), #home/ ---> como no tiene nada se redicrecciona al home 
    path('usuarios/', core_views.usuarios, name="usuarios"),
    path('medicinas/', core_views.medicinas, name="medicinas"),
    path('clientes/', core_views.clientes, name="clientes"),
    path('laboratorios/', core_views.laboratorios, name="laboratorios"),
    path('distribuidores/', core_views.distribuidores, name="distribuidores"),
    path('ventas/', core_views.ventas, name="ventas"),
    path('login/', core_views.login, name="login"),
    path('registro/', core_views.registro, name="registro"),
    path('admin/', admin.site.urls),

    
    path('medicamentos/', medicamentos_views.medicamentos, name="medicamentos"),

    
]
