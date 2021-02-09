from django.db import models
#from medicamentos.models import Medicina
#from laboratorios.models import Laboratorio
#from distribuidores.models import Distribuidor

# Create your models here.

class Pedido(models.Model):
    cantidad_pedida = models.IntegerField (verbose_name="Cantidad")
    total = models.DecimalField(max_digits = 5, decimal_places = 2,verbose_name="Total") 
    updated = models.DateTimeField(auto_now = True)
    created = models.DateTimeField(auto_now_add = True)
    
    
class Meta:
    verbose_name = "Pedido"
    verbose_name_plural = "Pedidos"
     # ordering = ["created"] #ordena por el atributo que uno requiere, puede haber 1 o mas atributo
    
def __str__(self):
    return self.cantidad_pedida #+ " con fecha: " + str(self.created) - Se muestra en la vista de Admin solo el atributo especificado