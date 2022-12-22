from django.db import models


class Post(models.Model):
    titulo=models.CharField(max_length=30)
    subtitulo=models.CharField(max_length=30,null=True)
    autor=models.CharField(max_length=30,null=True)
    fecha=models.DateField()
    texto=models.TextField(max_length=200)
    imagen=models.ImageField()

    def __str__(self):
        return self.titulo
    
