from django import forms
from .models import Psicologo

class PsicologoForm(forms.ModelForm):
    class Meta:
        model = Psicologo
        fields = ['rut', 'nombre', 'primer_apellido', 'segundo_apellido', 'email']
