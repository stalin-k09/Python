from django.shortcuts import render
from .models import Venta

# Create your views here.
def ventas(request):
    ventas = Venta.objects.all()
    return render(request, "ventas/ventas.html", {"ventas":ventas})