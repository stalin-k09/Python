from django.shortcuts import render, HttpResponse

#Crea tus vistas aqui

#Crea tus vistas aqui

def home(request):
    return render(request,"core/home.html")
    
def medicinas(request):
    return render(request,"core/medicinas.html")

def clientes(request):
    return render(request,"core/clientes.html")

def laboratorios(request):
    return render(request,"core/laboratorios.html")    

def distribuidores(request):
    return render(request,"core/distribuidores.html")

def usuarios(request):
    return render(request,"core/usuarios.html")

def ventas(request):
    return render(request,"core/ventas.html")

def login(request):
    return render(request,"core/login.html")

def registro(request):
    return render(request,"core/registro.html")


