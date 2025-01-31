from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.
class Articulo (models.Model):
    titulo = models.CharField(max_length= 255)
    descripcion= models.CharField(max_length= 255)
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    contenido = RichTextField()
    imagen= models.ImageField(upload_to='articulos', null=True, blank=True)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
    

class ImagenArticulo(models.Model):
    noticia= models.OneToOneField(Articulo, on_delete=models.CASCADE)
    imagen= models.ImageField(upload_to='articulos', null=True, blank=True)

