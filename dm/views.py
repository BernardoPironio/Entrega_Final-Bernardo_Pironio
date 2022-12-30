from django.shortcuts import render,redirect
from dm.forms import MensajeF
from dm.models import Mensaje
from blog.models import Post


def enviar_mensaje(request):
    usuario=request.user
    if request.method=='POST':
        form=MensajeF(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            receptor=informacion['receptor']
            mensaje=informacion['mensaje']
            emisor=usuario
            leido=False
            mensaje_completo=Mensaje(receptor=receptor,mensaje=mensaje,emisor=emisor,leido=leido)
            mensaje_completo.save()
            posts=Post.objects.all()
            cantidad_posts=0
            for post in posts:
                cantidad_posts+=1
            return redirect('inicio')
        else:
            return render(request, 'dm/enviar_mensaje.html',{'form':form, 'mensaje':'Mensaje enviado incorrectamente'})
    else:
        form=MensajeF()
        return render(request,'dm/enviar_mensaje.html',{'form':form})

def leer_mensaje(request):
    usuario=request.user
    mensajes=Mensaje.objects.filter(receptor=usuario)
    for mensaje in mensajes:
        mensaje.leido=True
        mensaje.save()
    return render(request, 'dm/leer_mensaje.html',{'mensajes':mensajes})
    

