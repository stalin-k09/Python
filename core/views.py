from django.shortcuts import render, HttpResponse

http_cabecera = """
<h1>Welcom</h1>
<ul>
    <li><a href="/">home</a></li>


</ul>

"""


# Create your views here.
def home(request):
    return HttpResponse ("<h1>Mi primera libreria</h1")
