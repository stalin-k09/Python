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
from clientes.urls import pathClientes

from distribuidores.urls import pathDistribuidores
from salidas.urls import pathSalidas
from compras.urls import pathCompras

urlpatterns = [
    path('', core_views.home, name="home"), #home/ ---> como no tiene nada se redicrecciona al home 
    path('usuarios/', core_views.usuarios, name="usuarios"),
    #path('ventas/', core_views.ventas, name="ventas"),
    path('login/', core_views.login, name="login"),
    path('registro/', core_views.registro, name="registro"),
    path('admin/', admin.site.urls),


    path("distribuidores/", include(pathDistribuidores)),

    path("medicamentos/", include(pathMedicinas)),
    path("laboratorios/", include(pathLaboratorios)),
    path("clientes/", include(pathClientes)),
    path("salidas/", include(pathSalidas)),
    path("compras/", include(pathCompras)),
]
