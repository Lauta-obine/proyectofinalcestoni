from django import forms
from django.contrib.auth.forms import UserChangeForm, AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from .models import Avatar


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class EditUserForm(UserChangeForm):
    email= forms. EmailField(required=True, label='Email')
    first_name= forms.CharField(required=True, label='Nombre')
    last_name= forms.CharField(required=True, label='Apellido')

    class Meta:
        model= User
        fields = ('email', 'first_name', 'last_name', 'password')

class AvatarForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ['imagen']
        
