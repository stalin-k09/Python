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
from core import views


urlpatterns = [
    path('', views.home, name="home"), #home/ ---> como no tiene nada se redicrecciona al home 
    path('usuarios/', views.usuarios, name="usuarios"),
    path('medicinas/', views.medicinas, name="medicinas"),
    path('clientes/', views.clientes, name="clientes"),
    path('clientes/', views.clientes, name="laboratorios"),
    path('clientes/', views.clientes, name="distribuidores"),
    path('clientes/', views.clientes, name="compras"),
    path('clientes/', views.clientes, name="ventas"),
    path('clientes/', views.clientes, name="login"),




    path('admin/', admin.site.urls),
]
