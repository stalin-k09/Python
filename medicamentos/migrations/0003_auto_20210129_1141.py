# Generated by Django 2.2.7 on 2021-01-29 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicamentos', '0002_auto_20210129_1139'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medicina',
            name='id_medicina',
        ),
        migrations.AddField(
            model_name='medicina',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
