from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from pedidos.models import Pedido, LineaPedido
from django.contrib import messages
from django.utils.html import strip_tags
from django.core.mail import send_mail

# Create your views here.

@login_required(login_url="/autenticacion/loguear")
def procesar_pedido(request):
    pedido=Pedido.objects.create(user=request.user)
    carrito=carrito(request)
    lineas_pedido=list()

    for key, value in carrito.carrito.items():
        lineas_pedido.append(LineaPedido(

            producto=key,
            cantidad=value["cantidad"],
            user=request.user,
            pedido=pedido

        ))

    LineaPedido.objects.bulk_create(lineas_pedido)  #Muchos Insert Into en bloques

    enviar_mail(
        
        pedido=pedido,
        lineas_pedido=lineas_pedido,
        nombreusuario=request.username,
        emailusuario=request.usermail,
               
    )

    messages.success(request, "El pedido se ha creado correctamente")
    return redirect("../tienda")


def enviar_mail(**kwargs):
    asunto="Gracias por el pedido"
    mensaje=render_to_string("emails/pedido.html",{
        "pedido":kwargs.get("pedido"),
        "lineas_pedido":kwargs.get("lineas_pedido"),
        "nombreusuario":kwargs.get("nombreusuario"),


    })

    mensaje_texto=strip_tags(mensaje)
    from_email="lulito131@gmail.com"
    #to=kwargs.get("emailusuario")
    to="freddy.mercado131@outlook.com"
    send_mail(asunto, mensaje_texto, from_email, [to],html_message=mensaje)
