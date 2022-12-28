from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class Post(models.Model):
    titulo=models.CharField(max_length=30)
    subtitulo=models.CharField(max_length=30,null=True)
    autor=models.CharField(max_length=30,null=True)
    fecha=models.DateField()
    texto=RichTextField()
    imagen=models.ImageField()

    def __str__(self):
        return self.titulo

class Avatar(models.Model):
    imagen=models.ImageField(upload_to='avatares')
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user}--{self.imagen}'

class Descripcion(models.Model):
    descripcion=models.TextField(max_length=100)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.descripcion}'
