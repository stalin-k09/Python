from django.contrib import admin
from django.urls import path
from core import views as core_views

#from distribuidores import views as distribuidores_views

from medicamentos import views as medicamentos_views
from laboratorios import views as laboratorios_views
from distribuidores import views as distribuidores_views
from clientes import views as clientes_views

from . import settings 


urlpatterns = [
    path('', core_views.home, name="home"), #home/ ---> como no tiene nada se redicrecciona al home 
    path('usuarios/', core_views.usuarios, name="usuarios"),
    path('medicinas/', core_views.medicinas, name="medicinas"),
    #path('clientes/', core_views.clientes, name="clientes"),
    path('distribuidores/', distribuidores_views.distribuidores, name="distribuidores"),
    path('ventas/', core_views.ventas, name="ventas"),
    path('login/', core_views.login, name="login"),
    path('registro/', core_views.registro, name="registro"),
    path('admin/', admin.site.urls),
    path('clientes/', clientes_views.clientes, name="clientes"),
    path('medicamentos/', medicamentos_views.medicamentos, name="medicamentos"),
    path('laboratorios/', laboratorios_views.laboratorios, name="laboratorios"),
    
]
