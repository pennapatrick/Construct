from django.db import models
from django.contrib.auth.models import AbstractUser

class Users(AbstractUser):
    CHOICES_CARGO = (('V', 'Vendedor'),
                    ('G', 'Gerente'))
    cargo = models.CharField(max_length=1, choices=CHOICES_CARGO)
