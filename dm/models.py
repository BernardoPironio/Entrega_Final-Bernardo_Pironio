from django.db import models
from django.conf import settings
from datetime import datetime
from django.contrib.auth.models import User

class Mensaje(models.Model):
    emisor=models.ForeignKey(User,on_delete=models.CASCADE,related_name='emisor')
    receptor=models.ForeignKey(User,on_delete=models.CASCADE,related_name='receptor')
    mensaje=models.TextField(max_length=10000)
    leido=models.BooleanField(default=False)

    def __str__(self):
        return f'{self.mensaje}--{self.leido}'