from django.urls import path
from .views import  index, about, crear_articulo, articulos, ArticuloDetailView, ArticuloDeleteView, ArticuloUpdateView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[

    path('inicio', index, name="inicio"),
    path('about', about, name="about"),
    path('crear-articulo', crear_articulo, name="crear_articulo"),
    path('articulos', articulos, name="articulos"),
    path('articulo/<int:pk>', ArticuloDetailView.as_view(), name='articulo_detail'),
    path('articulo/eliminar/<int:pk>', ArticuloDeleteView.as_view(), name='articulo_delete'),
    path('articulo/actualizar/<int:pk>', ArticuloUpdateView.as_view(), name='articulo_update'),


]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)