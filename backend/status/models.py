from django.db import models

class Status(models.Model):
    libelle = models.fields.CharField(max_length=100)
