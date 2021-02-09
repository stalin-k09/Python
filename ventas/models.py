from django.db import models
from clientes.models import Cliente
from medicamentos.models import Medicina
# Create your models here.

class Venta(models.Model):
    #id = models.AutoField (auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    cantidad_venta = models.IntegerField (verbose_name="Cantidad")
    total = models.DecimalField(max_digits = 5, decimal_places = 2,verbose_name="Total") 
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    #claves foraneas
    
    nombre_cliente = models.ForeignKey(Cliente, on_delete = models.CASCADE, verbose_name = "Nombre")
    #apellido_cliente = models.ForeignKey(Cliente, on_delete = models.CASCADE, verbose_name = "Apellido")
    nombre_comercial = models.ForeignKey(Medicina, on_delete = models.CASCADE, verbose_name="Nombre Medicamento")
    #precio = models.ForeignKey(Medicina,on_delete = models.CASCADE, verbose_name="Precio Venta")


    class Meta:
        verbose_name = "Venta"
        verbose_name_plural = "Ventas"
        # ordering = ["created"] #ordena por el atributo que uno requiere, puede haber 1 o mas atributo
    
    def __str__(self):
        return self.cantidad_venta #+ " con fecha: " + str(self.created) - Se muestra en la vista de Admin solo el atributo especificado