from django.contrib import admin
from .models import Medicina
# Register your models here.


class MedicinaAdmin(admin.ModelAdmin):
    readonly_fields = ["fecha_ingreso","fecha_modificacion"] #Muestra los datos pero no permite modificar


admin.site.register(Medicina, MedicinaAdmin)