from django.contrib import admin
from .models import Compra


class CompraAdmin(admin.ModelAdmin):
    readonly_fields = ["created","updated"]


# Register your models here.
admin.site.register(Compra, CompraAdmin)