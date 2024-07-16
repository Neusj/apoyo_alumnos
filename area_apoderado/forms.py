from django import forms
from .models import Apoderado

class ApoderadoForm(forms.ModelForm):
    class Meta:
        model = Apoderado
        fields = ['rut', 'nombre', 'primer_apellido', 'segundo_apellido','email']
