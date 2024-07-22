from django.db import models

from area_estudiante.models import Curso, Estudiante, TipoConducta


class Docente(models.Model):
    rut = models.CharField(max_length=12, primary_key=True)
    nombre = models.CharField(max_length=50)
    primer_apellido = models.CharField(max_length=50)
    segundo_apellido = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=100)
    id_curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.nombre} {self.primer_apellido} - {self.rut}'


class DatosAlumno(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    docente = models.ForeignKey(
        Docente, on_delete=models.CASCADE,
        default=''
    )
    tipo_conducta = models.ForeignKey(
        TipoConducta,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    descripcion = models.TextField(default='')