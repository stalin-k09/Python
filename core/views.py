
from django.shortcuts import render, HttpResponse
#hola
http_cabecera = """
<h1>Welcome</h1>
<h1>FarmaPro</h1>
<ul>

<li><a href="/">home</a></li>
 <li><a href="/presentacion">Presntacion</a></li>
<li><a href="/presentacion">Presntacion</a></li>
<li><a href="/contacto">Contacto</a></li>
<li><a href="/catalogo">Catalogo</a></li>




</ul>
"""


# Create your views here.
def home(request):
    return HttpResponse (http_cabecera+"<h1>Mi primera libreria</h1")

def presentacion(request):
    return HttpResponse (http_cabecera+"<h1>Hola integrantes del grupo  Stalin Carmen Luis Olm Luis Gar Georgi</h1")

def contacto(request):
    return HttpResponse (http_cabecera+"<h1>somos 6 integrantes</h1")

def catalogo(request):
    return HttpResponse (http_cabecera+"<h1>queremos pasar la materia</h1")
