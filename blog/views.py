from django.shortcuts import render,get_object_or_404, redirect
from blog.models import Post
from blog.forms import RegistroUsuario, PostF, EdicionUsuario

from django.contrib.auth.decorators import login_required as lr

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout,authenticate

from datetime import datetime as dt



def inicio(request):
    posts=Post.objects.all()
    return render(request, 'blog/inicio.html',{'posts':posts})

def about(request):
    return render(request, 'blog/about.html')

#parte de db

@lr
def crear(request):
    if request.method=='POST':
        form=PostF(request.POST or None, request.FILES or None)
        if form.is_valid():
            informacion=form.cleaned_data
            titulo=informacion['titulo']
            subtitulo=informacion['subtitulo']
            fecha=dt.now()
            autor=request.user.username
            texto=informacion['texto']
            imagen=informacion['imagen']
            post=Post(titulo=titulo,subtitulo=subtitulo,autor=autor,fecha=fecha,texto=texto,imagen=imagen)
            post.save()
            return redirect('inicio')
    else:
        form=PostF()
    return render(request, 'blog/crear.html', {'form': form})

def leer_mas(request,id):
    post=get_object_or_404(Post,id=id)
    return render(request,'blog/leer_mas.html',{'post':post})

def buscar(request):
    if request.GET['titulo']:
        titulo=request.GET['titulo']
        posts=Post.objects.filter(titulo__icontains=titulo)
        return render(request, 'blog/inicio.html', {'posts':posts})
    else:
        return render(request,'blog/inicio.html',{'mensaje':'No se a encontrado post','posts':posts})

@lr
def eliminar(request, id):
    post=Post.objects.get(id=id)
    if request.user.username==post.autor:
        post.delete()
    else:
        posts=Post.objects.all()
        return render(request, 'blog/inicio.html', {'mensaje':'Usted no creo el post, no es posible eliminarlo', 'posts':posts})
    return redirect('inicio')

@lr
def editar(request,id):
    post=Post.objects.get(id=id)
    if request.user.username==post.autor:
        if request.method=='POST':
            form=PostF(request.POST or None, request.FILES or None)
            if form.is_valid():
                informacion=form.cleaned_data
                post.titulo=informacion['titulo']
                post.subtitulo=informacion['subtitulo']
                post.fecha=dt.now()
                post.autor=request.user.username
                post.texto=informacion['texto']
                post.imagen=informacion['imagen']
                post.save()
                posts=Post.objects.all()
                return render(request, 'blog/inicio.html', {'posts':posts})
        else:
            form=PostF(initial={'titulo':post.titulo,'subtitulo':post.subtitulo,'texto':post.texto,'imagen':post.imagen})
        return render(request, 'blog/editar.html',{'form':form,'post':post})
    else:
        posts=Post.objects.all()
        return render(request, 'blog/inicio.html', {'mensaje':'Usted no creo el post, no es posible editarlo', 'posts':posts})
    

#parte de usuarios

def register(request):
    if request.method=='POST':
        form=RegistroUsuario(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            form.save()
            posts=Post.objects.all()
            return render(request, 'blog/inicio.html',{'mensaje':f'Usuario {username} creado correctamente','posts':posts})
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
                return redirect('inicio')
            else:
                return render(request, 'blog/login.html', {'form':form,'mensaje':'Usuario o Contraseña incorrectos'})
        else:
            return render(request, 'blog/login.html', {'form':form,'mensaje':'Usuario o Contraseña incorrectos'})
    else:
        form=AuthenticationForm()
    return render(request,'blog/login.html',{'form':form})

@lr
def perfil(request):
    posts=Post.objects.all()
    cantidad_de_posts=0
    for post in posts:
        if post.autor==request.user.username:
            cantidad_de_posts+=1
    return render(request, 'blog/perfil.html',{'cantidad_de_posts':cantidad_de_posts})

@lr
def editar_perfil(request):
    usuario=request.user
    if request.method=='POST':
        form=EdicionUsuario(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            usuario.username=informacion['username']    
            usuario.email=informacion['email']
            usuario.password1=informacion['password1']
            usuario.password2=informacion['password2']
            usuario.first_name=informacion['first_name']
            usuario.last_name=informacion['last_name']
            usuario.save()
            return render(request, 'blog/perfil.html',{'mensaje':'Usuario editado correctamente'})
        else:
            return render(request, 'blog/editar_perfil.html',{'form':form,'usuario':usuario,'mensaje':'Error al crear el perfil'})
    else:
        form=EdicionUsuario(initial={'username':usuario.username,'email':usuario.email,'first_name':usuario.first_name,'last_name':usuario.last_name})
    return render(request, 'blog/editar_perfil.html',{'form':form,'usuario':usuario})
    


