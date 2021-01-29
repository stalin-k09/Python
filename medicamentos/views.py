from django.shortcuts import render

# Create your views here.
from bdd.models import Medicina


def medicina(request):
    medicinas =Medicina.objects.all()
    return render(request,"../medicamentos/medicamentos/medicamentos.html", {"medicinas":medicinas})