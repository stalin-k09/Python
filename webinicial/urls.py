from django.contrib import admin
from django.urls import path, include
from core import views as core_views

#from distribuidores import views as distribuidores_views

from medicamentos import views as medicamentos_views
from laboratorios import views as laboratorios_views
from distribuidores import views as distribuidores_views
from clientes import views as clientes_views
from compras import views as compras_views

from . import settings 
from medicamentos.urls import pathMedicinas
from laboratorios.urls import pathLaboratorios

from distribuidores.urls import pathDistribuidores


urlpatterns = [
    path('', core_views.home, name="home"), #home/ ---> como no tiene nada se redicrecciona al home 
    path('usuarios/', core_views.usuarios, name="usuarios"),
    #path('clientes/', core_views.clientes, name="clientes"),
    #path('distribuidores/', distribuidores_views.distribuidores, name="distribuidores"),
    #path('ventas/', core_views.ventas, name="ventas"),
    path('login/', core_views.login, name="login"),
    path('registro/', core_views.registro, name="registro"),
    path('admin/', admin.site.urls),
    path('clientes/', clientes_views.clientes, name="clientes"),
    path('compras/', compras_views.compras, name="compras"),


    path("distribuidores/", include(pathDistribuidores)),

    path("medicamentos/", include(pathMedicinas)),
    path("laboratorios/", include(pathLaboratorios)),
]
