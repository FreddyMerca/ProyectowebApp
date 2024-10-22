from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Categoria(models.Model):
    
    nomCate=models.CharField(max_length=60) #Acordarse de la variable
    created=models.DateTimeField(auto_now=True)
    updated=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name='categoria'
        verbose_name_plural='categorias'
    
    def __str__(self):
        return self.nomCate

class Post(models.Model):
    
    titulo=models.CharField(max_length=60)
    contenido=models.CharField(max_length=60)
    imagen=models.ImageField(upload_to='blog', null=True, blank=True)
    autor=models.ForeignKey(User, on_delete=models.CASCADE) #Eliminar en cascada, se borra un usuario, borra todos sus POST
    categorias=models.ManyToManyField(Categoria)
    created=models.DateTimeField(auto_now=True)
    updated=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name='post'
        verbose_name_plural='posts'
    
    def __str__(self):
        return self.titulo