from django.urls import path

from . import views

app_name = "account_managers"

urlpatterns = [
    path("dashboard/", views.AccountManagerListView.as_view(), name="dashboard"),
    # path("contracts/", views.ContractsListView.as_view(), name="am_clients"),
]
