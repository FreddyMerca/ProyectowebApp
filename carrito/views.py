from django.shortcuts import render
from .carrito import carrito
from tienda.models import Producto
from django.shortcuts import redirect


# Create your views here.


def agregar_producto(request, producto_id):
    
    carrito_instancia=carrito(request)
    producto=Producto.objects.get(id=producto_id)
    carrito_instancia.agregar(producto=producto)
    return redirect("Tienda")

def eliminar_producto(request, producto_id):
    
    carrito_instancia=carrito(request)
    producto=Producto.objects.get(id=producto_id)
    carrito_instancia.eliminar(producto=producto)
    return redirect("Tienda")

def restar_producto(request, producto_id):
    
    carrito_instancia=carrito(request)
    producto=Producto.objects.get(id=producto_id)
    carrito_instancia.restar(producto=producto)
    return redirect("Tienda")

def limpiar_carro(request, producto_id):
    
    carrito_instancia=carrito(request)
    carrito_instancia.limpiar
    return redirect("Tienda")