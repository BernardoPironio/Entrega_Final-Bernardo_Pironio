from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from ckeditor.widgets import CKEditorWidget

class RegistroUsuario(UserCreationForm):
    email=forms.EmailField()
    username=forms.CharField(label='Ingrese nombre de Usuario')
    password1=forms.CharField(label='Ingrese Contraseña',widget=forms.PasswordInput)
    password2=forms.CharField(label='Repita Contraseña',widget=forms.PasswordInput)
    first_name=forms.CharField(label='Nombre')
    last_name=forms.CharField(label='Apellido')

    class Meta:
        model=User
        fields=['username','email','password1','password2','first_name','last_name']
        help_texts={k:'' for k in fields}


class EdicionUsuario(UserCreationForm):
    email=forms.EmailField()
    username=forms.CharField(label='Editar nombre de Usuario')
    password1=forms.CharField(label='Ingrese Nueva Contraseña',widget=forms.PasswordInput)
    password2=forms.CharField(label='Repita Contraseña',widget=forms.PasswordInput)
    first_name=forms.CharField(label='Editar Nombre')
    last_name=forms.CharField(label='Editar Apellido')

    class Meta:
        model=User
        fields=['username','email','password1','password2','first_name','last_name']
        help_texts={k:'' for k in fields}


class PostF(forms.Form):
    titulo=forms.CharField(max_length=30)
    subtitulo=forms.CharField(max_length=30)
    texto=forms.CharField(widget=CKEditorWidget())
    imagen=forms.ImageField()

class AvatarF(forms.Form):
    imagen=forms.ImageField(label='Imagen')

class DescripcionF(forms.Form):
    descripcion=forms.CharField(widget=forms.Textarea(attrs={'name':'descripcion','rows':10,'cols':100}))