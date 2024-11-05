from django.db import models
from django.conf import settings
from source.models import Source
from locality.models import Locality

class Maintenance(models.Model):
    ticket = models.CharField(max_length=100)
    designation = models.CharField(max_length=150)
    serialNumber = models.CharField(max_length=150)
    anomaly = models.CharField(max_length=100)
    status = models.CharField(max_length=50)
    observation = models.CharField(max_length=150)
    date_entree = models.fields.DateField(max_length=100)
    date_sortie = models.fields.DateField(max_length=100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)
    source = models.ForeignKey(Source, null=True, on_delete=models.SET_NULL)
    locality = models.ForeignKey(Locality, null=True, on_delete=models.SET_NULL)

