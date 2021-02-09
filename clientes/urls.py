from django.urls import path
from .views import (
    ClienteListView,
    ClienteCreateView,
    ClienteUpdateView,
    ClienteDeleteView,
)


pathClientes = (
    [
        path("", ClienteListView.as_view(), name="clientes"),
        path("create", ClienteCreateView.as_view(), name="create"),
        path("update/<int:pk>", ClienteUpdateView.as_view(), name="update"),
        path("delete/<int:pk>", ClienteDeleteView.as_view(), name="delete"),
    ],
    "clientes",
)