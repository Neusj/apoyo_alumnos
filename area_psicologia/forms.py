from django import forms
from .models import Psicologo, Reporte

class PsicologoForm(forms.ModelForm):
    class Meta:
        model = Psicologo
        fields = ['rut', 'nombre', 'primer_apellido', 'segundo_apellido', 'email']


class ReporteForm(forms.ModelForm):
    class Meta:
        model = Reporte
        fields = ['recomendacion', 'estado']
