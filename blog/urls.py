from django.urls import path
from blog.views import *
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', inicio ,name='inicio'),
    path('about/',about,name='about'),
    
    path('registrar/',register,name='register'),
    path('logear/',login_request,name='login'),
    path('deslogearse/',LogoutView.as_view(),name='logout'),
    path('perfil/',perfil,name='perfil'),
    path('editarperfil',editar_perfil,name='editar_perfil'),

    path('crear/',crear,name='crear'),
    path('leermas<id>/',leer_mas,name='leer_mas'),
    path('buscar/', buscar, name='buscar'),
    path('eliminar<id>/', eliminar, name='eliminar'),
    path('editar<id>/', editar,name='editar'),

    



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
