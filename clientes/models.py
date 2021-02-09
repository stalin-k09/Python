from django.db import models

# Create your models here.
class Cliente(models.Model):
    cedula = models.CharField(max_length = 10, verbose_name="Cédula")
    nombre_cliente = models.CharField(max_length = 50, verbose_name="Nombre")
    apellido_cliente = models.CharField(max_length = 50, verbose_name="Apellido")
    direccion_cliente = models.CharField(max_length = 50, verbose_name="Dirección")
    ciudad_cliente = models.CharField(max_length = 20, verbose_name="Ciudad")
    telefono_cliente = models.CharField(max_length = 10,verbose_name="teléfono")
    correo_cliente = models.EmailField(max_length = 50, verbose_name="Correo")
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)


    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        
        # ordering = ["created"] #ordena por el atributo que uno requiere, puede haber 1 o mas atributo
    
    def __str__(self):
        return self.nombre_cliente #+ " con fecha: " + str(self.created) - Se muestra en la vista de Admin solo el atributo especificado