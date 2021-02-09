from django.urls import path
from .views import (
    LaboratorioListView,
    LaboratorioCreateView,
    LaboratorioUpdateView,
    LaboratorioDeleteView,
)


pathLaboratorios = (
    [
        path("", LaboratorioListView.as_view(), name="laboratorios"),
        path("create", LaboratorioCreateView.as_view(), name="create"),
        path("update/<int:pk>", LaboratorioUpdateView.as_view(), name="update"),
        path("delete/<int:pk>", LaboratorioDeleteView.as_view(), name="delete"),
    ],
    "laboratorios",
)