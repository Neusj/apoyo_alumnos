from django.db import models

from area_estudiante.models import Estudiante


class Psicologo(models.Model):
    rut = models.CharField(max_length=12, primary_key=True)
    nombre = models.CharField(max_length=50)
    primer_apellido = models.CharField(max_length=50)
    segundo_apellido = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)


class Reporte(models.Model):
    id = models.AutoField(primary_key=True)
    rut_psicologo = models.ForeignKey(Psicologo, on_delete=models.CASCADE)
    rut_estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    recomendacion = models.TextField()
    estado = models.CharField(max_length=20)