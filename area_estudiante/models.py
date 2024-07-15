from django.db import models

from area_apoderado.models import Apoderado


class Curso(models.Model):
    nombre = models.CharField(max_length=50)
    año = models.PositiveIntegerField()
    seccion = models.CharField(max_length=10)


class TipoConducta(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()


class Estudiante(models.Model):
    rut = models.CharField(max_length=12, primary_key=True)
    nombre = models.CharField(max_length=50)
    primer_apellido = models.CharField(max_length=50)
    segundo_apellido = models.CharField(max_length=50)
    id_curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    apoderado = models.ForeignKey(Apoderado, on_delete=models.CASCADE)
    tipo_conducta = models.ForeignKey(TipoConducta, on_delete=models.CASCADE)
