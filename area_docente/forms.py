from django import forms
from .models import DatosAlumno, Docente

class DocenteForm(forms.ModelForm):
    class Meta:
        model = Docente
        fields = ['rut', 'nombre', 'primer_apellido', 'segundo_apellido','email', 'id_curso']


class DatosAlumnoForm(forms.ModelForm):
    class Meta:
        model = DatosAlumno
        fields = ['estudiante', 'tipo_conducta', 'descripcion', 'docente']

