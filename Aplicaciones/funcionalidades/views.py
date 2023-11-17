# En mi_app/views.py
from django.shortcuts import render
from .forms import SubirArchivoForm

def mostrar_contenido(request):
    contenido = None

    if request.method == 'POST':
        form = SubirArchivoForm(request.POST, request.FILES)
        if form.is_valid():
            archivo_cargado = request.FILES['archivo']
            contenido = archivo_cargado.read().decode('utf-8')
    else:
        form = SubirArchivoForm()

    return render(request, 'mostrar_contenido.html', {'form': form, 'contenido': contenido})
