from django.urls import path
from .views import (
    SalidaListView,
    SalidaCreateView,
    SalidaUpdateView,
    SalidaDeleteView,
)


pathSalidas = (
    [
        path("", SalidaListView.as_view(), name="salidas"),
        path("create", SalidaCreateView.as_view(), name="create"),
        path("update/<int:pk>", SalidaUpdateView.as_view(), name="update"),
        path("delete/<int:pk>", SalidaDeleteView.as_view(), name="delete"),
    ],
    "salidas",
)