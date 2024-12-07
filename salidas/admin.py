from django.contrib import admin
from .models import Salida


class SalidaAdmin(admin.ModelAdmin):
    readonly_fields = ["created","updated"]


# Register your models here.
admin.site.register(Salida, SalidaAdmin)