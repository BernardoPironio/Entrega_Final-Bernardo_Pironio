from django.shortcuts import render
from blog.models import Post
from blog.forms import RegistroUsuario, PostF

from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import login,logout,authenticate



def inicio(request):
    posts=Post.objects.all()
    return render(request, 'blog/inicio.html',{'posts':posts})

def about(request):
    return render(request, 'blog/about.html')

#parte de db

def crear(request):
    if request.method=='POST':
        form=PostF(request.POST, request.FILES)
        if form.is_valid():
            informacion=form.cleaned_data
            titulo=informacion['titulo']
            subtitulo=informacion['subtitulo']
            autor=informacion['autor']
            fecha=informacion['fecha']
            texto=informacion['texto']
            imagen=informacion['imagen']
            post=PostF(titulo=titulo,subtitulo=subtitulo,autor=autor,fecha=fecha,texto=texto,imagen=imagen)
            post.save()
            return render(request, 'blog/inicio.html',{'mensaje':'post creado correctamente'})
    else:
        formulario=PostF()
    return render(request, 'blog/crear.html', {'form': formulario})


#parte de usuarios

def register(request):
    if request.method=='POST':
        form=RegistroUsuario(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            form.save()
            return render(request, 'blog/inicio.html',{'mensaje':f'Usuario {username} creado correctamente'})
        else:
            return render(request, 'blog/register.html',{'form':form,'mensaje':'Error al crear el usuario'})
    else:
        form=RegistroUsuario()
    return render(request, 'blog/register.html',{'form':form})

def login_request(request):
    if request.method=='POST':
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            usu=form.cleaned_data.get('username')
            clave=form.cleaned_data.get('password')
            usuario=authenticate(username=usu,password=clave)
            if usuario is not None:
                login(request,usuario)
                return render(request, 'blog/inicio.html', {'mensaje':f'Bienvenido {usuario}, usuario logeado'})
            else:
                return render(request, 'blog/login.html', {'form':form,'mensaje':'Usuario o Contraseña incorrectos'})
        else:
            return render(request, 'blog/login.html', {'form':form,'mensaje':'Usuario o Contraseña incorrectos'})
    else:
        form=AuthenticationForm()
    return render(request,'blog/login.html',{'form':form})
