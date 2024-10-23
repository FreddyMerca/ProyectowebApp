from django.urls import path
from ProyectowebApp import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    
    path('inicio', views.inicio, name="Inicio"),
         
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
