# Generated by Django 2.2.7 on 2021-02-09 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_auto_20210208_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='correo_cliente',
            field=models.EmailField(max_length=50, verbose_name='Correo'),
        ),
    ]
