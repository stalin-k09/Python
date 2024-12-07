# from django.shortcuts import render

# # Create your views here.
# from .models import Medicina

# def medicamentos(request):
#     medicinas=Medicina.objects.all()
#     return render(request,"medicamentos/medicamentos.html", {"medicinas":medicinas})

from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Medicina
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

class MedicinaListView(ListView):
    model = Medicina


class MedicinaCreateView(CreateView):
    model = Medicina
    fields = ["nombre_comercial", "dci", "forma_farmaceutica","laboratorio","cantidad_unidades","precio","fecha_expiracion"]
    success_url = reverse_lazy("medicamentos:medicamentos")


class MedicinaUpdateView(UpdateView):
    model = Medicina
    fields = ["nombre_comercial", "dci", "forma_farmaceutica","laboratorio","cantidad_unidades","precio","fecha_expiracion"]
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return reverse_lazy("medicamentos:update", args=[self.object.id]) + "?ok"


class MedicinaDeleteView(DeleteView):
    model = Medicina
    success_url = reverse_lazy("medicamentos:medicamentos")
