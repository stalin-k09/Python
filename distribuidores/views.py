from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Distribuidor
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


class DistribuidorListView(ListView):
    model = Distribuidor


class DistribuidorCreateView(CreateView):
    model = Distribuidor
    fields = ["nombre_distribuidor", "ruc_distribuidor", "direccion_distribuidor","ciudad_distribuidor","telefono_distribuidor","correo_distribuidor"]
    success_url = reverse_lazy("distribuidores:distribuidores")


class DistribuidorUpdateView(UpdateView):
    model = Distribuidor
    fields = ["nombre_distribuidor", "ruc_distribuidor", "direccion_distribuidor","ciudad_distribuidor","telefono_distribuidor","correo_distribuidor"]
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return reverse_lazy("distribuidores:update", args=[self.object.id]) + "?ok"


class DistribuidorDeleteView(DeleteView):
    model = Distribuidor
    success_url = reverse_lazy("distribuidores:distribuidores")
