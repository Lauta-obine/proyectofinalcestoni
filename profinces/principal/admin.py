from django.contrib import admin

# Register your models here.
from .models import Articulo

@admin.register(Articulo)
class ArticuloAdmin(admin.ModelAdmin):
    list_display=('titulo','descripcion')
    search_fields=('tiutlo', 'descripcion')
    list_filter=['fecha_publicacion']
    ordering=['-fecha_publicacion']

