from django.db import models

class Laboratorio (models.Model):
    nombre_laboratorio = models.CharField(max_length=100, verbose_name="Laboratorio", blank=False, null=False, unique=True)
    direccion_laboratorio = models.TextField(max_length=200, verbose_name="Dirección", blank=False, null=False)
    telefono_laboratorio = models.IntegerField(max_length=10 ,verbose_name="Teléfono", blank=False, null=False )
    correo_laboratorio = models.EmailField( verbose_name="Correo", blank=False, null=False)
    registro_laboratorio = models.CharField(max_length=20, verbose_name="Registro", blank=False, null=False)
    autorizacion_laboratorio = models.CharField(max_length=20, verbose_name="Autorización", blank=False, null=False)

    class Meta:
        verbose_name ="Laboratorio"
        verbose_name_plural ="Laboratorios"

    def __str__(self):
        return self.nombre_laboratorio # Atributo que me muestra en la tabla del Admin