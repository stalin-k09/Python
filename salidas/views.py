from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Salida
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class SalidaListView(ListView):
    model = Salida


class SalidaCreateView(CreateView):
    model = Salida
    fields = ["medicamento","cliente","cantidad_venta"]
    success_url = reverse_lazy("salidas:salidas")


class SalidaUpdateView(UpdateView):
    model = Salida
    fields = ["medicamento","cliente","cantidad_venta"]
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return reverse_lazy("salidas:update", args=[self.object.id]) + "?ok"


class SalidaDeleteView(DeleteView):
    model = Salida
    success_url = reverse_lazy("salidas:salidas")