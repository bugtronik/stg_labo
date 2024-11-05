from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    CREATOR  = 'CREATOR'
    SUBSCRIBER = 'SUBSCRIBER'

    ROLE_CHOICES = (
        (CREATOR, 'Administrateur'),
        (SUBSCRIBER, 'Membre'),
    )
    role = models.CharField(max_length=30, choices=ROLE_CHOICES, verbose_name='Rôle')