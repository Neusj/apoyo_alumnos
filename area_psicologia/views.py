from django.contrib import messages
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import get_object_or_404, redirect, render

from area_psicologia.forms import PsicologoForm
from area_psicologia.models import Psicologo
from home.models import CustomUser
from home.utils.utils import is_administrador



@user_passes_test(is_administrador, login_url='home')
def psicologo_list(request):
    psicologos = Psicologo.objects.all()
    return render(request, 'psicologo_list.html', {'psicologos': psicologos})

@user_passes_test(is_administrador, login_url='home')
def psicologo_create(request):
    if request.method == 'POST':
        form = PsicologoForm(request.POST)
        if form.is_valid():
            rut = form.cleaned_data.get('rut')
            if CustomUser.objects.filter(username=rut).exists():
                messages.error(request, 'Ya existe un usuario con este RUT.')
                return render(request, 'docente_form.html', {'form': form})
            psicologo = form.save()
            CustomUser.objects.create_user(
                username=psicologo.rut,
                first_name=psicologo.nombre,
                last_name=psicologo.primer_apellido,
                password=psicologo.rut,
                tipo='psicologo'
            )
            return redirect('psicologo_list')
    else:
        form = PsicologoForm()
    return render(request, 'psicologo_form.html', {'form': form})

@user_passes_test(is_administrador, login_url='home')
def psicologo_update(request, pk):
    psicologo = get_object_or_404(Psicologo, pk=pk)
    if request.method == 'POST':
        form = PsicologoForm(request.POST, instance=psicologo)
        if form.is_valid():
            form.save()
            return redirect('psicologo_list')
    else:
        form = PsicologoForm(instance=psicologo)
    return render(request, 'psicologo_form.html', {'form': form})

def psicologo_delete(request, pk):
    psicologo = get_object_or_404(Psicologo, pk=pk)
    if request.method == 'POST':
        try:
            psicologo.delete()
            messages.success(request, "Psicologo eliminado correctamente.")
            return redirect('psicologo_list')
        except ValidationError as e:
            messages.error(request, str(e))
            return redirect('psicologo_list')
    return render(request, 'psicologo_confirm_delete.html', {'psicologo': psicologo})
