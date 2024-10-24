from django.db import models

# Create your models here.


class CategoriaProd(models.Model):

    nombreCate=models.CharField(max_length=60)
    created=models.DateTimeField(auto_now=True)
    updated=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name='categoriaProd'
        verbose_name_plural='categoriasProd'
    
    def __str__(self):
        return self.nombreCate
    

class Producto(models.Model):

    nombre=models.CharField(max_length=60)
    categoria=models.ForeignKey(CategoriaProd, on_delete=models.CASCADE)    
    imagen=models.ImageField(upload_to="tienda", null=True, blank=True)
    precio=models.FloatField()
    disponibilidad=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now=True)
    updated=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name='Producto'
        verbose_name_plural='Productos'

