# Generated by Django 2.2.7 on 2021-01-29 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medicina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_comercial', models.CharField(max_length=100, unique=True, verbose_name='Nombre')),
                ('dci', models.CharField(max_length=100, unique=True, verbose_name='DCI')),
                ('forma_farmaceutica', models.CharField(max_length=50, verbose_name='Forma Farmacéutica')),
                ('cantidad_unidades', models.IntegerField(verbose_name='Cantidad')),
                ('precio', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Precio Unidad')),
                ('fecha_ingreso', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Ingreso')),
                ('fecha_expiracion', models.DateField(verbose_name='Fecha de Expiración')),
                ('fecha_modificacion', models.DateTimeField(auto_now=True, verbose_name='Última Modificación')),
            ],
            options={
                'verbose_name': 'Medicina',
                'verbose_name_plural': 'Medicinas',
            },
        ),
    ]
