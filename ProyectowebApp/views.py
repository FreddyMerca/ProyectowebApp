from django.shortcuts import render

# Create your views here.

def inicio(request):

    return render(request,"ProyectowebApp/inicio.html")

def tienda(request):

    return render(request,"ProyectowebApp/tienda.html")




