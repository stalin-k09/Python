from django.db import models


class Laboratorio (models.Model):
    nombre_laboratorio = models.CharField(max_length=100, verbose_name="Laboratorio", blank=False, null=False, unique=True)
    direccion_laboratorio = models.TextField(max_length=200, verbose_name="Dirección", blank=False, null=False)
    telefono_laboratorio = models.BigIntegerField(verbose_name="Teléfono", blank=False, null=False )
    correo_laboratorio = models.EmailField( verbose_name="Correo", blank=False, null=False)
    registro_laboratorio = models.CharField(max_length=200, verbose_name="Registro", blank=False, null=False)
    autorizacion_laboratorio = models.CharField(max_length=200, verbose_name="Autorización", blank=False, null=False)

    class Meta:
        verbose_name ="Laboratorio"
        verbose_name_plural ="Laboratorios"

    def __str__(self):
        return self.nombre_laboratorio # Atributo que me muestra en la tabla del Admin

class Medicina (models.Model):
    nombre_comercial = models.CharField(max_length=100, verbose_name="Nombre", blank=False, null=False, unique=True)
    dci = models.CharField(max_length=100, verbose_name="DCI", blank=False, null=False, unique=True)
    forma_farmaceutica = models.CharField(max_length=50, verbose_name="Forma Farmacéutica", blank=False, null=False)
    #laboratorio = models.ForeignKey(Laboratorio,on_delete=models.CASCADE, verbose_name="Laboratorio")
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


class Distribuidor(models.Model):
    nombre_distribuidor = models.CharField(max_length = 50, verbose_name="Nombre Destribuidor" , blank=False, null=False, unique=True)
    ruc_distribuidor = models.IntegerField(verbose_name="RUC", blank=False, null=False)
    direccion_distribuidor = models.CharField(max_length = 50,verbose_name="Dirección", blank=False, null=False)
    ciudad_distribuidor = models.CharField(max_length = 50,erbose_name="Ciudad", blank=False, null=False)
    telefono_distribuidor = models.IntegerField(verbose_name="Teléfono", blank=False, null=False)
    correo_distribuidor = models.CharField(max_length = 50,verbose_name="Correo", blank=False, null=False)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)

    class Meta:
        verbose_name = "Distribuidor"
        verbose_name_plural = "Distribuidores"
        
        # ordering = ["created"] #ordena por el atributo que uno requiere, puede haber 1 o mas atributo
    
    def __str__(self):
        return self.nombre_distribuidor #+ " con fecha: " + str(self.created) - Se muestra en la vista de Admin solo el atributo especificado