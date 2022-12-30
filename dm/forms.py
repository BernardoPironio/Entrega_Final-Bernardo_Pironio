from django import forms
from django.contrib.auth.models import User

class MensajeF(forms.Form):
    receptor=forms.ModelChoiceField(User.objects.all())
    mensaje=forms.CharField(max_length=10000)