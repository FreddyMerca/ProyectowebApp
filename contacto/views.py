from django.shortcuts import render, redirect
from .forms import FormContacto
from django.core.mail import EmailMessage


# Create your views here.

def contacto(request):

    formulario_contacto=FormContacto()

    if request.method=="POST":
        formulario_contacto=FormContacto(data=request.POST)
        if formulario_contacto.is_valid():
            nombre=request.POST.get("nombre")
            email=request.POST.get("email")
            asunto=request.POST.get("asunto")
            contenido=request.POST.get("contenido")


            email = EmailMessage("Mensaje: {}".format(asunto), "El usuario con Nombre {} con la dirección {} escribe lo siguiente:\n\n{}".format(nombre, email, contenido),["lulito131@gmail.com"], reply_to=[email])



            #email=EmailMessage("Mensaje{}","El usuario con Nombre {} con la direccion {} escribe lo siguiente:\n\n {}", format(asunto, nombre, email, contenido),["lulito131@gmail.com"], reply_to=[email])

            try:
                email.send()
                
                return redirect("/contacto/?valido")
            
            except:

                return redirect("/contacto/?novalido")

    return render(request,"contacto/contacto.html", {'miFormulario':formulario_contacto})
