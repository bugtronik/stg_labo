from django.db import models
from django.conf import settings
from source.models import Source
from locality.models import Locality

class Hotline(models.Model):
    ticket = models.CharField(max_length=100)
    designation = models.CharField(max_length=150)
    serialNumber = models.CharField(max_length=150)
    anomaly = models.CharField(max_length=100)
    date_entree = models.fields.DateField(max_length=100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)
    source = models.ForeignKey(Source, null=True, on_delete=models.SET_NULL)
    locality = models.ForeignKey(Locality, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)
    date_update = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=150, blank=True)
    isMaintenance = models.CharField(max_length=10)