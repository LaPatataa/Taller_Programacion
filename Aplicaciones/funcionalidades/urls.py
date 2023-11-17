# En mi_app/urls.py
from django.urls import path
from .views import mostrar_contenido

urlpatterns = [
    path('mostrar_contenido/', mostrar_contenido, name='mostrar_contenido'),
    # ... otras rutas ...
]
