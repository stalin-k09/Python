from django.shortcuts import render

# Create your views here.
from bdd.models import Distribuidor


def distribuidor(request):
    distribuidores =Distribuidor.objects.all()
    return render(request,"../distribuidores/distribuidores/distribuidores.html", {"distribuidores":distribuidores})