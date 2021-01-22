from django.shortcuts import render, HttpResponse

#Crea tus vistas aqui

#Crea tus vistas aqui

def home(request):
    return render(request,"core/home.html")
    
def medicinas(request):
    return render(request,"core/medicinas.html")

def clientes(request):
    return render(request,"core/clientes.html")

def usuarios(request):
    return render(request,"core/laboratorios.html")    

def usuarios(request):
    return render(request,"core/distribuidores.html")

def usuarios(request):
    return render(request,"core/compra.html")

def usuarios(request):
    return render(request,"core/venta.html")

def usuarios(request):
    return render(request,"core/login.html")


