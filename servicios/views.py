from django.shortcuts import render
from django.shortcuts import render, HttpResponse
from servicios.models import Servicio

# Create your views here.

def servicios(request):

    servicios=Servicio.objects.all()
    return render(request,"servicios/servicios.html", {"servicios": servicios})