from django.db import models
from django.core.exceptions import ValidationError


class Apoderado(models.Model):
    rut = models.CharField(max_length=12, primary_key=True)
    nombre = models.CharField(max_length=50)
    primer_apellido = models.CharField(max_length=50)
    segundo_apellido = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return f'{self.rut} {self.nombre} {self.primer_apellido}'
    
    def delete(self, *args, **kwargs):
        if self.estudiante_set.exists():
            raise ValidationError("No se puede borrar el apoderado porque hay estudiantes asociados.")
        super().delete(*args, **kwargs)