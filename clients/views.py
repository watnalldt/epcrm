from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.generic import DetailView, ListView

from contracts.models import Contract
from core.views import HTMLTitleMixin

from .models import Client


@method_decorator([never_cache], name="dispatch")
class AMClientContractsView(LoginRequiredMixin, HTMLTitleMixin, DetailView):
    model = Client
    template_name = "clients/contracts/am_contracts.html"
    login_url = "/users/login/"

    def get_html_title(self):
        return self.object.client

    def get_queryset(self, *args, **kwargs):
        return (
            super()
            .get_queryset(*args, **kwargs)
            .filter(account_manager__account_manager=self.request.user)
        )

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     contract = Contract.objects.get(pk=self.kwargs["pk"])
    #     client_contracts = Client.objects.filter(client=contract.client).filter(
    #         account_manager__account_manager=self.request.user
    #     )
    #     context["client_contracts"] = client_contracts
    #     return context
