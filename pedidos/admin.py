from django.contrib import admin
from .models import Pedido
# Register your models here.

class PedidoAdmin(admin.ModelAdmin):
    readonly_fields = ["created","updated"]
admin.site.register(Pedido, PedidoAdmin)