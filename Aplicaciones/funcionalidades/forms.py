# En mi_app/forms.py
from django import forms

class SubirArchivoForm(forms.Form):
    archivo = forms.FileField()
