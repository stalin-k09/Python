from django.shortcuts import render

from .models import Compra

# Create your views here.
def compras(request):
    compras=Compra.objects.all()
    return render(request,"compras/compras.html", {"compras":compras})