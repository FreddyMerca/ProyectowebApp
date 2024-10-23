from django.shortcuts import render
from .models import Producto

# Create your views here.

def tienda(request):

    productos=Producto.objects.all() #variable productos que toma todo lo que esta en el modelo Prodcuto de la clase creada en Models.py

    return render(request,"tienda/tienda.html", {"productos":productos}) #se crea un diccinario que le ponemos de nombre productos que trae lo que esta en la varableproductos

