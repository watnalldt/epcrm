from django.urls import path

from . import views

app_name = "contracts"

urlpatterns = [
    path("contract_list/", views.ContractListView.as_view(), name="contract_list"),
    path(
        "account_manager/contract_detail/<pk>/",
        views.AMContractDetailView.as_view(),
        name="am_contract_detail",
    ),
    path(
        "client_manager/contract_detail/<pk>/",
        views.CMContractDetailView.as_view(),
        name="cm_contract_detail",
    ),
    path("pdf/<pk>", views.contracts_render_pdf_view, name="contract_pdf_view"),
]
