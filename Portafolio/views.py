from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def inicio(request):
    """Retorna gestion pagina de inicio"""
    return render(request,"pages/inicio.html",{})

def resumen(request):
    """Retorna gestion pagina de inicio"""
    return render(request,"pages/resumen.html",{})

