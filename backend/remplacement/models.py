from django.db import models

from django.db import models
from django.conf import settings

class Remplacement(models.Model):
    ancien = models.CharField(max_length=100)
    etat = models.CharField(max_length=150)
    cause = models.CharField(max_length=150)
    nouveau = models.CharField(max_length=100)
    ticket = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)


