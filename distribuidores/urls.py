from django.urls import path
from .views import (
    DistribuidorListView,
    DistribuidorCreateView,
    DistribuidorDeleteView,
    DistribuidorUpdateView,
)


pathDistribuidores = (
    [
        path("", DistribuidorListView.as_view(), name="distribuidores"),
        path("create", DistribuidorCreateView.as_view(), name="create"),
        path("update/<int:pk>", DistribuidorUpdateView.as_view(), name="update"),
        path("delete/<int:pk>", DistribuidorDeleteView.as_view(), name="delete"),
    ],
    "distribuidores",
)