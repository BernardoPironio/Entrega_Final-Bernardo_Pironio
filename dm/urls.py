from django.urls import path
from dm.views import *
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   path('enviarmensaje/',enviar_mensaje,name='enviar_mensaje'),
   path('leermensajes/',leer_mensaje,name='leer_mensaje'),


]
