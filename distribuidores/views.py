from django.shortcuts import render

from .models import Distribuidor

def distribuidores(request):
    distribuidores=Distribuidor.objects.all()
    return render(request,"distribuidores/distribuidores.html", {"distribuidores":distribuidores})