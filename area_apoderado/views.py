from django.shortcuts import render, get_object_or_404, redirect
from .models import Apoderado
from .forms import ApoderadoForm

# Create your views here.

def apoderado_list(request):
    apoderados = Apoderado.objects.all()
    return render(request, 'apoderado_list.html', {'apoderados': apoderados})

def apoderado_create(request):
    if request.method == 'POST':
        form = ApoderadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('apoderado_list')
    else:
        form = ApoderadoForm()
    return render(request, 'apoderado_form.html', {'form': form})

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
        apoderado.delete()
        return redirect('apoderado_list')
    return render(request, 'apoderado_confirm_delete.html', {'apoderado': apoderado})
