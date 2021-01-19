from django.shortcuts import render, HttpResponse

# Create your views here.

def medicamentos(request):
    return HttpResponse(html_cabecera + "<h1>Medicamentos FARMAPRO</h1>")