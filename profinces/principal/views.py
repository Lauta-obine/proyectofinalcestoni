from django.shortcuts import render, redirect
from .forms import ArticuloFormulario
from django.contrib.auth.forms import AuthenticationForm,  PasswordChangeForm
from django.contrib.auth.decorators import login_required
from principal.models import Articulo
from django.views.generic import DetailView, DeleteView, UpdateView
from django.contrib.auth import authenticate
from django.urls import reverse_lazy
# Create your views here.

def index (request):
    return render (request,"index.html")

def about (request):
    return render (request,"about.html")
@login_required
def crear_articulo(request):
    if request.method == "POST":
        form=ArticuloFormulario(request.POST, request.FILES)
        if form.is_valid():
            form.save(user=request.user)
            return redirect("articulos")
    else:
        form = ArticuloFormulario()
    return render (request,"crear_articulo.html",{"form":form})

def articulos (request):
    lista_articulos= Articulo.objects.all()
 
 
    return render(request,"articulos.html",{"Articulos":lista_articulos})

class ArticuloDetailView(DetailView):
    model=Articulo
    template_name='articulo_detail.html'
    context_object_name="articulo"

class ArticuloDeleteView(DeleteView):
    model=Articulo
    template_name='articulo_delete.html'
    success_url = reverse_lazy('articulos')
class ArticuloUpdateView(UpdateView):
    model= Articulo
    fields=['titulo', 'descripcion','contenido', 'imagen']
    template_name= 'articulo_update.html'
    success_url = reverse_lazy('articulos')

      







