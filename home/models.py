from django.db import models

from django.contrib.auth.models import AbstractUser
from django.db import models



class CustomUser(AbstractUser):
    TIPO_CHOICES = [
        ('administrador', 'Administrador'),
        ('docente', 'Docente'),
        ('apoderado', 'Apoderado'),
        ('psicologo', 'Psicólogo'),
    ]

    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES, default='alumno')
