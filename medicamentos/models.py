from django.db import models
from laboratorios.models import Laboratorio


# Create your models here.
class Medicina (models.Model):
    nombre_comercial = models.CharField(max_length=100, verbose_name="Nombre", blank=False, null=False, unique=True)
    dci = models.CharField(max_length=100, verbose_name="DCI", blank=False, null=False, unique=True)
    forma_farmaceutica = models.CharField(max_length=50, verbose_name="Forma Farmacéutica", blank=False, null=False)
    laboratorio = models.ForeignKey(Laboratorio,on_delete=models.CASCADE, verbose_name="Laboratorio")
    cantidad_unidades = models.IntegerField(verbose_name="Cantidad", blank=False, null=False )
    precio = models.DecimalField(max_digits = 5, decimal_places = 2,verbose_name="Precio Unidad", blank=False, null=False)
    fecha_ingreso = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Ingreso")
    fecha_expiracion = models.DateField(verbose_name="Fecha de Expiración", blank=False, null=False)
    fecha_modificacion = models.DateTimeField(auto_now=True, verbose_name="Última Modificación")

    
    class Meta:
        verbose_name = "Medicina"
        verbose_name_plural = "Medicinas"
        # ordering = ["created"] #ordena por el atributo que uno requiere, puede haber 1 o mas atributo
    
    def __str__(self):
        return self.nombre_comercial #+ " con fecha: " + str(self.created) - Se muestra en la vista de Admin solo el atributo especificado