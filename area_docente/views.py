from django.contrib import messages
from django.forms import ValidationError
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import user_passes_test
from area_docente.forms import DatosAlumnoForm, DocenteForm
from area_docente.models import DatosAlumno, Docente
from home.models import CustomUser
from home.utils.utils import is_administrador


@user_passes_test(is_administrador, login_url='home')
def docente_list(request):
    docentes = Docente.objects.all()
    return render(request, 'docente_list.html', {'docentes': docentes})

@user_passes_test(is_administrador, login_url='home')
def docente_create(request):
    if request.method == 'POST':
        form = DocenteForm(request.POST)
        if form.is_valid():
            rut = form.cleaned_data.get('rut')
            if CustomUser.objects.filter(username=rut).exists():
                messages.error(request, 'Ya existe un usuario con este RUT.')
                return render(request, 'docente_form.html', {'form': form})


            docente = form.save()
            CustomUser.objects.create_user(
                username=docente.rut,
                first_name=docente.nombre,
                last_name=docente.primer_apellido,
                password=docente.rut,
                tipo='docente'
            )
            return redirect('docente_list')
    else:
        form = DocenteForm()
    return render(request, 'docente_form.html', {'form': form})

@user_passes_test(is_administrador, login_url='home')
def docente_update(request, pk):
    docente = get_object_or_404(Docente, pk=pk)
    if request.method == 'POST':
        form = DocenteForm(request.POST, instance=docente)
        if form.is_valid():
            form.save()
            return redirect('docente_list')
    else:
        form = DocenteForm(instance=docente)
    return render(request, 'docente_form.html', {'form': form})

def docente_delete(request, pk):
    docente = get_object_or_404(Docente, pk=pk)
    if request.method == 'POST':
        try:
            docente.delete()
            messages.success(request, "Docente eliminado correctamente.")
            return redirect('docente_list')
        except ValidationError as e:
            messages.error(request, str(e))
            return redirect('docente_list')
    return render(request, 'docente_confirm_delete.html', {'docente': docente})



def datos_alumno_list(request):
    datos_alumno = DatosAlumno.objects.all()
    return render(request, 'datos_alumno_list.html', {'datos_alumno': datos_alumno})


def datos_alumno_create(request):
    if request.method == 'POST':
        form = DatosAlumnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('datos_alumno_list')
    else:
        form = DatosAlumnoForm()
    return render(request, 'datos_alumno_form.html', {'form': form})


def datos_alumno_update(request, pk):
    datos_alumno = get_object_or_404(DatosAlumno, pk=pk)
    if request.method == 'POST':
        form = DatosAlumnoForm(request.POST, instance=datos_alumno)
        if form.is_valid():
            form.save()
            return redirect('datos_alumno_list')
    else:
        form = DatosAlumnoForm(instance=datos_alumno)
    return render(request, 'datos_alumno_form.html', {'form': form})

def datos_alumno_delete(request, pk):
    datos_alumno = get_object_or_404(DatosAlumno, pk=pk)
    if request.method == 'POST':
        datos_alumno.delete()
        return redirect('datos_alumno_list')
    return render(request, 'datos_alumno_confirm_delete.html', {'datos_alumno': datos_alumno})


def datos_alumno_ver(request, pk):
    datos_alumno = get_object_or_404(DatosAlumno, pk=pk)
    return render(request, 'datos_alumno_ver.html', {'datos_alumno': datos_alumno})
