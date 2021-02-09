from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Compra
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class CompraListView(ListView):
    model = Compra


class CompraCreateView(CreateView):
    model = Compra
    fields = ["nombre_medicamento","nombre_laboratorio","nombre_distribuidor","cantidad_compra"]
    success_url = reverse_lazy("compras:compras")


class CompraUpdateView(UpdateView):
    model = Compra
    fields = ["nombre_medicamento","nombre_laboratorio","nombre_distribuidor","cantidad_compra"]
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return reverse_lazy("compras:update", args=[self.object.id]) + "?ok"


class CompraDeleteView(DeleteView):
    model = Compra
    success_url = reverse_lazy("compras:compras")
