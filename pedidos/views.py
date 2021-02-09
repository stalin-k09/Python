from django.shortcuts import render
from .models import Pedido

# Create your views here.
def pedidos(request):
    pedidos = Pedido.objects.all()
    return render(request, "pedidos/pedidos.html", {"pedidos":pedidos})