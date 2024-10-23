from django.shortcuts import render
from .carrito import carrito
from tienda.models import Producto
from django.shortcuts import redirect


# Create your views here.


def agregar_producto(request, producto_id):
    
    carrito=carrito(request)
    producto=Producto.objects.get(id=producto_id)
    carrito.agregar(producto=producto)
    return redirect("tienda")

def eliminar_producto(request, producto_id):
    
    carrito=carrito(request)
    producto=Producto.objects.get(id=producto_id)
    carrito.eliminar(producto=producto)
    return redirect("tienda")

def restar_producto(request, producto_id):
    
    carrito=carrito(request)
    producto=Producto.objects.get(id=producto_id)
    carrito.restar_producto(producto=producto)
    return redirect("tienda")

def limpiar_carro(request, producto_id):
    
    carrito=carrito(request)
    carrito.limpiar_carro
    return redirect("tienda")