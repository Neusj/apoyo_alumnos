from django.shortcuts import render, get_object_or_404, redirect

from home.models import CustomUser
from home.utils.utils import is_administrador
from .models import Apoderado
from .forms import ApoderadoForm
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import user_passes_test


@user_passes_test(is_administrador, login_url='home')
def apoderado_list(request):
    apoderados = Apoderado.objects.all()
    return render(request, 'apoderado_list.html', {'apoderados': apoderados})

@user_passes_test(is_administrador, login_url='home')
def apoderado_create(request):
    if request.method == 'POST':
        form = ApoderadoForm(request.POST)
        if form.is_valid():
            rut = form.cleaned_data.get('rut')
            if CustomUser.objects.filter(username=rut).exists():
                messages.error(request, 'Ya existe un usuario con este RUT.')
                return render(request, 'apoderado_form.html', {'form': form})
            
            apoderado = form.save()
            CustomUser.objects.create_user(
                username=apoderado.rut,
                first_name=apoderado.nombre,
                last_name=apoderado.primer_apellido,
                password=apoderado.rut,
                tipo='apoderado'
            )
            return redirect('apoderado_list')
    else:
        form = ApoderadoForm()
    return render(request, 'apoderado_form.html', {'form': form})

@user_passes_test(is_administrador, login_url='home')
def apoderado_update(request, pk):
    apoderado = get_object_or_404(Apoderado, pk=pk)
    if request.method == 'POST':
        form = ApoderadoForm(request.POST, instance=apoderado)
        if form.is_valid():
            form.save()
            return redirect('apoderado_list')
    else:
        form = ApoderadoForm(instance=apoderado)
    return render(request, 'apoderado_form.html', {'form': form})

def apoderado_delete(request, pk):
    apoderado = get_object_or_404(Apoderado, pk=pk)
    if request.method == 'POST':
        try:
            apoderado.delete()
            messages.success(request, "Apoderado eliminado correctamente.")
            return redirect('apoderado_list')
        except ValidationError as e:
            messages.error(request, str(e))
            return redirect('apoderado_list')
    return render(request, 'apoderado_confirm_delete.html', {'apoderado': apoderado})
