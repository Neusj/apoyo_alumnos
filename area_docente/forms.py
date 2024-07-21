from django import forms
from .models import Docente

class DocenteForm(forms.ModelForm):
    class Meta:
        model = Docente
        fields = ['rut', 'nombre', 'primer_apellido', 'segundo_apellido','email', 'id_curso']


