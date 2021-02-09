from django.contrib import admin
from .models import Venta
# Register your models here.

class VentaAdmin(admin.ModelAdmin):
    readonly_fields = ["created","updated"]
admin.site.register(Venta, VentaAdmin)