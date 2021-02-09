from django.db import models
from medicamentos.models import Medicina
from clientes.models import Cliente

# Create your models here.

class Salida(models.Model):
    updated = models.DateTimeField(auto_now = True)
    created = models.DateTimeField(auto_now_add = True)
    #claves foraneas
    medicamento = models.ForeignKey(Medicina, on_delete = models.CASCADE, verbose_name="Medicamento")

    cliente = models.ForeignKey(Cliente, on_delete = models.CASCADE, verbose_name="Cliente")
    
    cantidad_venta = models.IntegerField (verbose_name="Cantidad")

    
class Meta:
        verbose_name = "Venta"
        verbose_name_plural = "Ventas"
        # ordering = ["created"] #ordena por el atributo que uno requiere, puede haber 1 o mas atributo
    