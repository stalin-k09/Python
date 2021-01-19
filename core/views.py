from django.shortcuts import render, HttpResponse

# Create your views here.
#Hola
def medicamentos(request):
    return HttpResponse(html_cabecera + "<h1>Medicamentos FARMAPRO - QuitSoft </h1>")