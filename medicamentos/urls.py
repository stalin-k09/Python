from django.urls import path
from .views import (
    MedicinaListView,
    MedicinaCreateView,
    MedicinaUpdateView,
    MedicinaDeleteView,
)


pathMedicinas = (
    [
        path("", MedicinaListView.as_view(), name="medicamentos"),
        path("create", MedicinaCreateView.as_view(), name="create"),
        path("update/<int:pk>", MedicinaUpdateView.as_view(), name="update"),
        path("delete/<int:pk>", MedicinaDeleteView.as_view(), name="delete"),
    ],
    "medicamentos",
)