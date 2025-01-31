from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import EditUserForm, LoginForm, UserRegistrationForm, AvatarForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm,  PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from .models import Avatar






def register_view(request):
    if request.user.is_authenticated:
        return redirect('inicio')  
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('inicio')
    else:
        form = UserRegistrationForm()
    return render(request, 'registrar.html', {'form': form})

def perfil(request):
    return render(request, "perfil.html")

@login_required
def editar_perfil(request):
    if request.method == "POST":

        form = EditUserForm(request.POST, instance=request.user)
        try:
            avatar= request.user.avatar
        except Avatar.DoesNotExist:
            avatar=None
        if avatar:
            avatar_form= AvatarForm(request.POST, request.FILES, instance=avatar)  
        else:
            avatar_form= AvatarForm(request.POST, request.FILES)

        if  form.is_valid() and avatar_form.is_valid():
            form.save()
            avatar_instance = avatar_form.save(commit=False)
            avatar_instance.user = request.user
            avatar_instance.save()

            
            return redirect("accounts:perfil")
        
    else: 
        form = EditUserForm(instance=request.user)
        if hasattr(request.user, "avatar"):
            avatar_form=AvatarForm(instance= request.user.avatar)
        else:
            avatar_form= AvatarForm()

    return render(request, "editar_perfil.html", {"form": form, "avatar_form": avatar_form})
        

def login_view(request):
    if request.user.is_authenticated:
        return redirect('inicio') 

    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('inicio')  
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('inicio')

@login_required
def cambiar_contrasena(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if  form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('contrasena_cambiada')
    else: 
        form= PasswordChangeForm(request.user)
    return render (request, 'cambiar_contra.html', {'form': form})

@login_required
def contrasena_cambiada(request):
    return render(request, 'contrasena_cambuiada.html')

    