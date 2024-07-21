from django.db import models

from area_estudiante.models import Curso


class Docente(models.Model):
    rut = models.CharField(max_length=12, primary_key=True)
    nombre = models.CharField(max_length=50)
    primer_apellido = models.CharField(max_length=50)
    segundo_apellido = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    id_curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
