from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Cliente
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class ClienteListView(ListView):
    model = Cliente


class ClienteCreateView(CreateView):
    model = Cliente
    fields = ["cedula","nombre_cliente","apellido_cliente","direccion_cliente","ciudad_cliente","telefono_cliente","correo_cliente"]
    success_url = reverse_lazy("clientes:clientes")


class ClienteUpdateView(UpdateView):
    model = Cliente
    fields = ["cedula","nombre_cliente","apellido_cliente","direccion_cliente","ciudad_cliente","telefono_cliente","correo_cliente"]
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return reverse_lazy("clientes:update", args=[self.object.id]) + "?ok"


class ClienteDeleteView(DeleteView):
    model = Cliente
    success_url = reverse_lazy("clientes:clientes")