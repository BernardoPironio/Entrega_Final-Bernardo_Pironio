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

    path('crear/',crear,name='crear'),
    path('leermas<id>/',leer_mas,name='leer_mas'),
    



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
