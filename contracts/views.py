from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.template.loader import get_template
from django.views.generic import DetailView, ListView
from xhtml2pdf import pisa

from core.views import HTMLTitleMixin

from .models import Contract

User = get_user_model()


class ContractListView(LoginRequiredMixin, HTMLTitleMixin, ListView):
    model = Contract
    context_object_name = "contracts"
    template_name = "contracts/contract_list.html"
    login_url = "/users/login/"
    html_title = "Total Contracts"


class ContractDetailView(LoginRequiredMixin, HTMLTitleMixin, DetailView):
    model = Contract
    template_name = "contracts/contract_detail.html"

    def get_html_title(self):
        return self.object.business_name


class AMContractDetailView(LoginRequiredMixin, HTMLTitleMixin, DetailView):
    model = Contract
    template_name = "contracts/contract_detail.html"
    login_url = "/users/login/"

    def get_queryset(self, *args, **kwargs):
        return (
            super()
            .get_queryset(*args, **kwargs)
            .filter(account_manager__account_manager=self.request.user)
        )

    def get_html_title(self):
        return self.object.business_name


class CMContractDetailView(LoginRequiredMixin, HTMLTitleMixin, DetailView):
    model = Contract
    template_name = "contracts/contract_detail.html"
    login_url = "/users/login/"

    def get_queryset(self, *args, **kwargs):
        return (
            super()
            .get_queryset(*args, **kwargs)
            .filter(client_manager__client_manager=self.request.user)
        )

    def get_html_title(self):
        return self.site_name


@login_required(login_url="/users/login/")
def contracts_render_pdf_view(request, *args, **kwargs):
    pk = kwargs.get("pk")
    contract = get_object_or_404(
        Contract, pk=pk, account_manager__account_manager=request.user
    )

    template_path = "contracts/generate_pdf.html"
    context = {"contract": contract}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type="application/pdf")

    # to directly download the pdf we need attachment
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'

    # to view on browser we can remove attachment
    response["Content-Disposition"] = 'filename="report.pdf"'

    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse("We had some errors <pre>" + html + "</pre>")
    return response
