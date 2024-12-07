from django.db import models
from medicamentos.models import Medicina
from laboratorios.models import Laboratorio
from distribuidores.models import Distribuidor

# Create your models here.

class Compra(models.Model):
    cantidad_compra = models.IntegerField (verbose_name="Cantidad")
    updated = models.DateTimeField(auto_now = True)
    created = models.DateTimeField(auto_now_add = True)
    #claves foraneas
    nombre_medicamento = models.ForeignKey(Medicina, on_delete = models.CASCADE, verbose_name="Nombre Medicamento")
    nombre_laboratorio = models.ForeignKey(Laboratorio, on_delete = models.CASCADE, verbose_name="Nombre Laboratorio")
    nombre_distribuidor = models.ForeignKey(Distribuidor, on_delete = models.CASCADE, verbose_name="Nombre Distribuidor")
    

    
class Meta:
        verbose_name = "Compra"
        verbose_name_plural = "Compras"
        # ordering = ["created"] #ordena por el atributo que uno requiere, puede haber 1 o mas atributo
    
def __str__(self):
    return self.cantidad_compra #+ " con fecha: " + str(self.created) - Se muestra en la vista de Admin solo el atributo especificado