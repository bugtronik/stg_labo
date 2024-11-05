from django.db import models

class Locality(models.Model):
    name = models.fields.CharField(max_length=100)
