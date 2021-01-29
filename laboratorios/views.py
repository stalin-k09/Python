from django.shortcuts import render

# Create your views here.
# Create your views here.
from .models import Laboratorio

def laboratorios(request):
    laboratorios=Laboratorio.objects.all()
    return render(request,"laboratorios/laboratorios.html", {"laboratorios":laboratorios})