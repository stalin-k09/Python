from django.shortcuts import render

# Create your views here.
from bdd.models import Medicina

def medicamentos(request):
    medicinas=Medicina.objects.all()
    return render(request,"medicamentos.html", {"medicinas":medicinas})