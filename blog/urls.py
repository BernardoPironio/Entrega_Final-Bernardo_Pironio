from django.urls import path
from blog.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', inicio ,name='inicio'),
    path('about/',about,name='about'),
    
    path('registrar/',register,name='register'),
    path('logear/',login_request,name='login'),
    path('deslogearse/',LogoutView.as_view(),name='logout'),

    path('crear/',crear,name='crear'),
]
