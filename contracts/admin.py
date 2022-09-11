from admin_auto_filters.filters import AutocompleteFilter
from django.contrib import admin
from import_export import fields, resources
from import_export.admin import ImportExportModelAdmin
from import_export.widgets import ForeignKeyWidget
from rangefilter.filters import DateRangeFilter

from account_managers.models import AccountManager
from client_managers.models import ClientManager
from clients.models import Client
from utilities.models import Supplier, Utility

from .models import Contract


class ContractResource(resources.ModelResource):

    client = fields.Field(
        column_name="client",
        attribute="client",
        widget=ForeignKeyWidget(Client, "client"),
    )

    account_manager = fields.Field(
        column_name="account_manager",
        attribute="account_manager",
        widget=ForeignKeyWidget(AccountManager, "account_manager__email"),
    )

    client_manager = fields.Field(
        column_name="client_manager",
        attribute="client_manager",
        widget=ForeignKeyWidget(ClientManager, "client_manager__email"),
    )

    supplier = fields.Field(
        column_name="supplier",
        attribute="supplier",
        widget=ForeignKeyWidget(Supplier, "supplier"),
    )

    utility = fields.Field(
        column_name="utility",
        attribute="utility",
        widget=ForeignKeyWidget(Utility, "utility"),
    )

    class Meta:
        model = Contract
        skip_unchanged = True
        report_skipped = True
        import_id_fields = ("id",)


class ClientFilter(AutocompleteFilter):
    title = "Client"  # display title
    field_name = "client"  # name of the foreign key field


class SupplierFilter(AutocompleteFilter):
    title = "Supplier"  # display title
    field_name = "supplier"  # name of the foreign key field


class AMFilter(AutocompleteFilter):
    title = "Account Manager"  # display title
    field_name = "account_manager"  # name of the foreign key field


class UtilityTypeFilter(AutocompleteFilter):
    title = "Utility Type"  # display title
    field_name = "utility"  # name of the foreign key field

    def get_rangefilter_contract_end_date_title(self, request, field_path):
        return "Contract End Date"

    def get_rangefilter_contract_start_date_title(self, request, field_path):
        return "Contract Start Date"


class ContractAdmin(ImportExportModelAdmin):
    show_full_result_count = False
    resource_class = ContractResource
    list_per_page = 10
    list_display = (
        "id",
        "business_name",
        "client",
        "site_address",
        "supplier",
        "utility",
        "meter_serial_number",
        "mpan_mpr",
        "eac",
        "contract_start_date",
        "contract_end_date",
        "is_ooc",
        "is_directors_approval",
        "vat",
    )
    fieldsets = (
        (
            "Site Information",
            {
                "description": "Enter the site details",
                "fields": (
                    ("client", "business_name"),
                    "site_address",
                    "supplier",
                    "utility",
                    "meter_serial_number",
                    "mpan_mpr",
                    "top_line",
                    "vat",
                ),
            },
        ),
        (
            "Contract Management Information",
            {
                "description": "Choose Account Manager & Client Manager",
                "fields": (
                    (
                        "account_manager",
                        "client_manager",
                        "account_number",
                        "company_reg_number",
                    ),
                    "is_directors_approval",
                    "seamless",
                    "non_seamless",
                ),
            },
        ),
        (
            "Contract Date Details",
            {
                "description": "Enter the following details",
                "fields": (
                    (
                        "contract_start_date",
                        "contract_end_date",
                        "contract_duration_months",
                    ),
                    "is_ooc",
                ),
            },
        ),
        (
            "Seamless Contract Information",
            {
                "description": "The following only applies to seamless contracts",
                "classes": ("collapse",),
                "fields": (
                    (
                        "dwellent_id",
                        "bid_id",
                        "property_reference",
                        "collector_id",
                        "portal_status",
                    ),
                    ("building_name", "billing_address"),
                    ("day_consumption", "contract_value"),
                    ("standing_charge", "service_charge_frequency"),
                    ("unit_rate_1", "unit_rate_2", "unit_rate_3", "unit_rate_4"),
                    "seamless_status",
                ),
            },
        ),
        (
            "Service Information",
            {
                "description": "Enter the following data",
                "fields": ("eac", "profile", "service_type", "feed_in_tariff"),
            },
        ),
        (
            "Rates",
            {
                "description": "Enter the following data",
                "fields": (
                    "pence_per_kilowatt",
                    "day_kilowatt_hour_rate",
                    "night_rate",
                    "standard_charge_monthly",
                    "annualised_budget",
                ),
            },
        ),
        (
            "Commissons",
            {
                "description": "Enter the following",
                # Enable a Collapsible Section
                "classes": ("collapse",),
                "fields": (
                    "commission_per_annum",
                    "commission_per_unit",
                    "total_commission_per_contract",
                    "partner_commission",
                ),
            },
        ),
        ("Notes", {"description": "Additional Information", "fields": ("notes",)}),
    )
    list_filter = [
        "non_seamless",
        "seamless",
        ClientFilter,
        AMFilter,
        SupplierFilter,
        UtilityTypeFilter,
        "is_ooc",
        "is_directors_approval",
        ("contract_end_date", DateRangeFilter),
        ("contract_start_date", DateRangeFilter),
        "contract_duration_months",
        "vat",
    ]
    search_help_text = (
        "Search by MPAN/MPR or Business Name, Client Name, Meter Serial Number"
    )
    search_fields = (
        "business_name",
        "client__client",
        "mpan_mpr",
        "contract_end_date",
        "meter_serial_number",
        "site_address",
    )
    ordering = ["-contract_end_date"]
    date_hierarchy = "contract_end_date"


admin.site.register(Contract, ContractAdmin)
