from django.shortcuts import render
from .forms import FormContacto

# Create your views here.

def contacto(request):

    formulario_contacto=FormContacto()
    return render(request,"contacto/contacto.html", {'miFormulario':formulario_contacto})
