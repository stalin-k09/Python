from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Laboratorio
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.

# def pages(request):
#     pages = get_list_or_404(
#         Page
#     )  # Otra alternativa para obtener todos los objetos de mi modelo
#     return render(request, "pages/pages.html", {"pages": pages})

class LaboratorioListView(ListView):
    model = Laboratorio


class LaboratorioCreateView(CreateView):
    model = Laboratorio
    fields = ["nombre_laboratorio","direccion_laboratorio","telefono_laboratorio","correo_laboratorio","registro_laboratorio","autorizacion_laboratorio"]
    success_url = reverse_lazy("laboratorios:laboratorios")


class LaboratorioUpdateView(UpdateView):
    model = Laboratorio
    fields = ["nombre_laboratorio","direccion_laboratorio","telefono_laboratorio","correo_laboratorio","registro_laboratorio","autorizacion_laboratorio"]
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return reverse_lazy("laboratorios:update", args=[self.object.id]) + "?ok"


class LaboratorioDeleteView(DeleteView):
    model = Laboratorio
    success_url = reverse_lazy("laboratorios:laboratorios")
