from django.db import models

# Create your models here.

class Cliente(models.Model):
    cedula = models.IntegerField(verbose_name="Cédula")
    nombre_cliente = models.CharField(max_length = 50, verbose_name="Nombre")
    apellido_cliente = models.CharField(max_length = 50, verbose_name="Apellido")
    ciudad_cliente = models.CharField(max_length = 20, verbose_name="Ciudad")
    provincia_cliente = models.CharField(max_length = 50, verbose_name="Provincia")
    direccion_cliente = models.CharField(max_length = 50, verbose_name="Apellido")
    telefono_cliente = models.IntegerField (verbose_name="telefono")
    correo_cliente = models.CharField(max_length = 50, verbose_name="Correo")
    fechanac_cliente = models.DateTimeField(verbose_name="Fecha de Nacimiento")
    estado_cliente = models.CharField(max_length = 3, verbose_name="Estado")



class Pedido(models.Model):
    cantidad = models.IntegerField (verbose_name="Cantidad")
    total = models.IntegerField (verbose_name="Total")
    estado_pedido = models.CharField(max_length = 3, verbose_name="Estado Pedido")
    

class Medicamento(models.Model):
    nombre_medicamento = models.CharField(max_length = 50, verbose_name="Nombre Medicamento")
    descripcion_medicamento = models.CharField(max_length = 50, verbose_name="Descripción")
    categoria_medicamento = models.CharField(max_length = 20, verbose_name="Categoria")
    fecha_produccion = models.DateTimeField(verbose_name="Fecha de Producción")
    fecha_expiracion = models.DateTimeField(verbose_name="Fecha de Expiración")
    tipo_medicamento = models.CharField(max_length = 30, verbose_name="Tipo de Medicamento")
    precio_compra = models.DecimalField (verbose_name="Precio de Compra")
    precio_venta = models.DecimalField (verbose_name="Precio de Venta")
    stock = models.CharField(max_length = 30, verbose_name="Stock")
    estado_cliente = models.CharField(max_length = 3, verbose_name="Estado")