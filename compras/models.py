from django.db import models
from .models import Medicamento
from .models import Laboratorio
from .models import Distribuidor

# Create your models here.

class Compra(models.Model):
    cantidad_compra = models.IntegerField (verbose_name="Cantidad")
    updated = models.DateTimeField(auto_now = True)
    created = models.DateTimeField(auto_now_add = True)
    #claves foraneas
    nombre_medicamento = models.ForeignKey(Medicamento, on_delete = models.CASCADE, verbose_name="Nombre Medicamento")
    nombre_laboratorio = models.ForeignKey(Laboratorio, on_delete = models.CASCADE, verbose_name="Nombre Laboratorio")
    nombre_distribuidor = models.ForeignKey(Distribuidor, on_delete = models.CASCADE, verbose_name="Nombre Distribuidor")
    

    
class Meta:
        verbose_name = "Compra"
        verbose_name_plural = "Compras"
        # ordering = ["created"] #ordena por el atributo que uno requiere, puede haber 1 o mas atributo
    
def __str__(self):
    return self.nombre_medicamento #+ " con fecha: " + str(self.created) - Se muestra en la vista de Admin solo el atributo especificado