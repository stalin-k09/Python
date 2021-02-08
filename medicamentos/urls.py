# from django.urls import path
# from .views import (
#     MedicamentoListView,
#     MedicamentoCreateView,
#     MedicamentoUpdateView,
#     MedicamentoDeleteView,
# )


# pathPages = (
#     [
#         path("", MedicamentoListView.as_view(), name="medicamentos"),
#         # Utilizar la clave primaria no olvidar utilizar el pk
#         path("create", MedicamentoCreateView.as_view(), name="create"),
#         path("update/<int:pk>", MedicamentoUpdateView.as_view(), name="update"),
#         path("delete/<int:pk>", MedicamentoDeleteView.as_view(), name="delete"),
#     ],
#     "pages",
# )