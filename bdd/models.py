from django.db import models


# class Distribuidor(models.Model):
#     nombre_distribuidor = models.CharField(max_length = 50, verbose_name="Nombre Destribuidor" , blank=False, null=False, unique=True)
#     ruc_distribuidor = models.IntegerField(verbose_name="RUC", blank=False, null=False)
#     direccion_distribuidor = models.CharField(max_length = 50,verbose_name="Dirección", blank=False, null=False)
#     ciudad_distribuidor = models.CharField(max_length = 50,verbose_name="Ciudad", blank=False, null=False)
#     telefono_distribuidor = models.IntegerField(verbose_name="Teléfono", blank=False, null=False)
#     correo_distribuidor = models.CharField(max_length = 50,verbose_name="Correo", blank=False, null=False)
#     created = models.DateTimeField(auto_now_add = True)
#     updated = models.DateTimeField(auto_now = True)

#     class Meta:
#         verbose_name = "Distribuidor"
#         verbose_name_plural = "Distribuidores"
        
#         # ordering = ["created"] #ordena por el atributo que uno requiere, puede haber 1 o mas atributo
    
#     def __str__(self):
#         return self.nombre_distribuidor #+ " con fecha: " + str(self.created) - Se muestra en la vista de Admin solo el atributo especificado