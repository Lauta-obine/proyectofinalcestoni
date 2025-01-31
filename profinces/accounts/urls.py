from django.urls import path
from .views import  editar_perfil, perfil, login_view, logout_view, register_view, cambiar_contrasena, contrasena_cambiada
from django.conf import settings
from django.conf.urls.static import static

app_name="accounts"


urlpatterns=[
    path("perfil", perfil, name="perfil"),
    path("editar-perfil", editar_perfil, name="editar_perfil"),
    path('login', login_view, name='login'),
    path('logout', logout_view, name='logout'),
    path('registrar', register_view, name='registrar'),
    path('cambiar-contrasena', cambiar_contrasena, name='cambiar_contrasena'),
    path('contrasena-cambiada', contrasena_cambiada, name='contrasena_cambiada'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)