from django.shortcuts import render, HttpResponse

html_cabecera = """
    <h1>Welcome</h1>
    <ul>
        <li><a href="/">Home</a></li>
        <li><a href="/">Distribuidores</a></li>
    </ul>
"""

#Create your views here.add()
def home (request):
    return HttpResponse(html_cabecera + "<h1> HOME PAGE</h1>")

def distribuidores (request):
    return HttpResponse(html_cabecera + "<h1> MODULO DISTRIBUIDORES</h1>")
