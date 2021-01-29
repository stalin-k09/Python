from django.contrib import admin
from .models import Distribuidor
# Register your models here.

class DistribuidorAdmin(admin.ModelAdmin):
    readonly_fields = ["created","updated"]
admin.site.register(Distribuidor, DistribuidorAdmin)