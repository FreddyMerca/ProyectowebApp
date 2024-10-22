from django import forms


class FormContacto(forms.Form):
    
    nombre=forms.CharField(label="Nombre", max_length=100, required=True)
    #email=forms.CharField(label="Email" max_length=100 required=True)
    email=forms.EmailField()
    asunto=forms.CharField(label="Asunto", max_length=100, required=True)
    contenido=forms.CharField(label="Contenido", widget=forms.Textarea, required=True,)

    #your_name = forms.CharField(label="Your name", max_length=100)