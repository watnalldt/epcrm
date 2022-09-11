from django.urls import path

from . import views

app_name = "clients"

urlpatterns = [
    path(
        "clients_contracts/<int:pk>/",
        views.AMClientContractsView.as_view(),
        name="am_clients_contracts",
    ),
]
