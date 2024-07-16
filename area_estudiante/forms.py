from django import forms
from .models import Curso, TipoConducta, Estudiante

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nombre', 'año', 'seccion']

class TipoConductaForm(forms.ModelForm):
    class Meta:
        model = TipoConducta
        fields = ['nombre', 'descripcion']

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ['rut', 'nombre', 'primer_apellido', 'segundo_apellido', 'id_curso', 'apoderado', 'tipo_conducta']
