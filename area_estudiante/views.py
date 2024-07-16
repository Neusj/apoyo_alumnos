from django.shortcuts import render, get_object_or_404, redirect
from .models import Curso, TipoConducta, Estudiante
from .forms import CursoForm, TipoConductaForm, EstudianteForm

# Curso
def curso_list(request):
    cursos = Curso.objects.all()
    return render(request, 'curso_list.html', {'cursos': cursos})

def curso_create(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('curso_list')
    else:
        form = CursoForm()
    return render(request, 'curso_form.html', {'form': form})

def curso_update(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    if request.method == 'POST':
        form = CursoForm(request.POST, instance=curso)
        if form.is_valid():
            form.save()
            return redirect('curso_list')
    else:
        form = CursoForm(instance=curso)
    return render(request, 'curso_form.html', {'form': form})

def curso_delete(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    if request.method == 'POST':
        curso.delete()
        return redirect('curso_list')
    return render(request, 'curso_confirm_delete.html', {'curso': curso})

# TipoConducta
def tipo_conducta_list(request):
    tipo_conductas = TipoConducta.objects.all()
    return render(request, 'tipo_conducta_list.html', {'tipo_conductas': tipo_conductas})

def tipo_conducta_create(request):
    if request.method == 'POST':
        form = TipoConductaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tipo_conducta_list')
    else:
        form = TipoConductaForm()
    return render(request, 'tipo_conducta_form.html', {'form': form})

def tipo_conducta_update(request, pk):
    tipo_conducta = get_object_or_404(TipoConducta, pk=pk)
    if request.method == 'POST':
        form = TipoConductaForm(request.POST, instance=tipo_conducta)
        if form.is_valid():
            form.save()
            return redirect('tipo_conducta_list')
    else:
        form = TipoConductaForm(instance=tipo_conducta)
    return render(request, 'tipo_conducta_form.html', {'form': form})

def tipo_conducta_delete(request, pk):
    tipo_conducta = get_object_or_404(TipoConducta, pk=pk)
    if request.method == 'POST':
        tipo_conducta.delete()
        return redirect('tipo_conducta_list')
    return render(request, 'tipo_conducta_confirm_delete.html', {'tipo_conducta': tipo_conducta})

# Estudiante
def estudiante_list(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'estudiante_list.html', {'estudiantes': estudiantes})

def estudiante_create(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('estudiante_list')
    else:
        form = EstudianteForm()
    return render(request, 'estudiante_form.html', {'form': form})

def estudiante_update(request, pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    if request.method == 'POST':
        form = EstudianteForm(request.POST, instance=estudiante)
        if form.is_valid():
            form.save()
            return redirect('estudiante_list')
    else:
        form = EstudianteForm(instance=estudiante)
    return render(request, 'estudiante_form.html', {'form': form})

def estudiante_delete(request, pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    if request.method == 'POST':
        estudiante.delete()
        return redirect('estudiante_list')
    return render(request, 'estudiante_confirm_delete.html', {'estudiante': estudiante})
