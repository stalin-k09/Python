from django.urls import path
from .views import (
    CompraListView,
    CompraCreateView,
    CompraUpdateView,
    CompraDeleteView,
)


pathCompras = (
    [
        path("", CompraListView.as_view(), name="compras"),
        path("create", CompraCreateView.as_view(), name="create"),
        path("update/<int:pk>", CompraUpdateView.as_view(), name="update"),
        path("delete/<int:pk>", CompraDeleteView.as_view(), name="delete"),
    ],
    "compras",
)