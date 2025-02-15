# Generated by Django 2.2.7 on 2021-02-09 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laboratorios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laboratorio',
            name='autorizacion_laboratorio',
            field=models.CharField(max_length=20, verbose_name='Autorización'),
        ),
        migrations.AlterField(
            model_name='laboratorio',
            name='registro_laboratorio',
            field=models.CharField(max_length=20, verbose_name='Registro'),
        ),
        migrations.AlterField(
            model_name='laboratorio',
            name='telefono_laboratorio',
            field=models.BigIntegerField(max_length=10, verbose_name='Teléfono'),
        ),
    ]
