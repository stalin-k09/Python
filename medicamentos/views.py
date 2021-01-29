from django.shortcuts import render

# Create your views here.
from .models import Medicina

def medicamentos(request):
    medicinas=Medicina.objects.all()
    return render(request,"medicamentos/medicamentos.html", {"medicinas":medicinas})