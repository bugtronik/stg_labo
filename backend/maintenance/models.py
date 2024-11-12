from django.db import models
from django.conf import settings
from hotline.models import Hotline
from status.models import Status

class Maintenance(models.Model):
    diagnostic = models.CharField(max_length=150)
    observation = models.CharField(max_length=150)
    date_entree = models.fields.DateField(max_length=100)
    date_sortie = models.fields.DateField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)
    updated_by = models.CharField(max_length=150, blank=True)
    hotline = models.ForeignKey(Hotline, null=True, on_delete=models.SET_NULL)
    status = models.ForeignKey(Status, null=True, on_delete=models.SET_NULL)