from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistroUsuario(UserCreationForm):
    email=forms.EmailField()
    username=forms.CharField(label='Ingrese nombre de Usuario')
    password1=forms.CharField(label='Ingrese Contraseña',widget=forms.PasswordInput)
    password2=forms.CharField(label='Repita Contraseña',widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=['username','email','password1','password2']
        help_texts={k:'' for k in fields}