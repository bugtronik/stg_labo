from django.db import models

class Source(models.Model):
    name = models.fields.CharField(max_length=100)
