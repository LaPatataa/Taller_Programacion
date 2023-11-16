from django.db import models

# Create your models here.


class Proyecto(models.Model):
    codigo = models.CharField(primary_key=True,max_length=4)
    nombre = models.CharField(max_length=90)
    descripcion = models.CharField( max_length=2000 )
    publish = models.BooleanField(default=True)
    date = models.DateField(auto_now=True)
    imageproj = models.FileField(upload_to='proyectos/',null=True)

def __str__(self) -> str:
    texto = "[{1}]{0}"
    if self.publish:
        tp = "On"
    else:
        tp = "off"
    return texto.format(self.nombre,tp)