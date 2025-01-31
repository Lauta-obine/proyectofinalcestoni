from django import forms
from .models import Articulo, ImagenArticulo
from django.contrib.auth.models import User
from ckeditor.widgets import CKEditorWidget


class ArticuloFormulario(forms.ModelForm):

    class Meta:
        model= Articulo
        fields = ['titulo', 'descripcion','contenido', 'imagen']

  

    def  save(self, user, commit=True):
        articulo= super().save(commit=False)
        articulo.user = user
        if commit:
            articulo.save()
        return articulo 


class ImagenForm(forms.ModelForm):
    class Meta:
        model = ImagenArticulo
        fields = ['imagen']
        
        
