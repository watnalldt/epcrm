# Generated by Django 4.1.1 on 2022-09-11 08:15

import django.db.models.deletion
import simple_history.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("account_managers", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("client_managers", "0001_initial"),
        ("utilities", "0001_initial"),
        ("clients", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="HistoricalContract",
            fields=[
                (
                    "id",
                    models.BigIntegerField(
                        auto_created=True, blank=True, db_index=True, verbose_name="ID"
                    ),
                ),
                ("created_at", models.DateTimeField(blank=True, editable=False)),
                ("updated_at", models.DateTimeField(blank=True, editable=False)),
                ("seamless", models.BooleanField(default=False)),
                ("non_seamless", models.BooleanField(default=False)),
                (
                    "dwellent_id",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("bid_id", models.CharField(blank=True, max_length=100, null=True)),
                ("portal_status", models.URLField(blank=True, null=True)),
                ("is_directors_approval", models.BooleanField(default=False)),
                ("business_name", models.CharField(max_length=255)),
                (
                    "company_reg_number",
                    models.CharField(blank=True, max_length=20, null=True),
                ),
                ("top_line", models.CharField(max_length=30)),
                ("mpan_mpr", models.CharField(max_length=255)),
                (
                    "meter_serial_number",
                    models.CharField(blank=True, max_length=30, null=True),
                ),
                (
                    "building_name",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("site_address", models.CharField(max_length=255)),
                (
                    "billing_address",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "account_number",
                    models.CharField(blank=True, max_length=30, null=True),
                ),
                ("contract_start_date", models.DateField(blank=True, null=True)),
                ("contract_end_date", models.DateField(blank=True, null=True)),
                (
                    "contract_duration_months",
                    models.IntegerField(blank=True, null=True),
                ),
                ("is_ooc", models.BooleanField(default=False)),
                ("eac", models.CharField(max_length=30)),
                (
                    "day_consumption",
                    models.CharField(blank=True, max_length=30, null=True),
                ),
                (
                    "night_consumption",
                    models.CharField(blank=True, max_length=30, null=True),
                ),
                ("profile", models.CharField(blank=True, max_length=30, null=True)),
                (
                    "service_type",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                (
                    "feed_in_tariff",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                ("pence_per_kilowatt", models.IntegerField(blank=True, null=True)),
                (
                    "day_kilowatt_hour_rate",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                ("night_rate", models.CharField(blank=True, max_length=30, null=True)),
                (
                    "standard_charge_monthly",
                    models.CharField(blank=True, max_length=30, null=True),
                ),
                (
                    "annualised_budget",
                    models.CharField(blank=True, max_length=30, null=True),
                ),
                (
                    "commission_per_annum",
                    models.CharField(blank=True, max_length=30, null=True),
                ),
                (
                    "commission_per_unit",
                    models.CharField(blank=True, max_length=30, null=True),
                ),
                (
                    "total_commission_per_contract",
                    models.CharField(blank=True, max_length=30, null=True),
                ),
                (
                    "partner_commission",
                    models.CharField(blank=True, max_length=30, null=True),
                ),
                ("vat", models.CharField(blank=True, max_length=10, null=True)),
                (
                    "contract_value",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                (
                    "standing_charge",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                (
                    "service_charge_frequency",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "unit_rate_1",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "unit_rate_2",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "unit_rate_3",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "unit_rate_4",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "seamless_status",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "smart_meter",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("notes", models.TextField(blank=True, null=True)),
                ("history_id", models.AutoField(primary_key=True, serialize=False)),
                ("history_date", models.DateTimeField(db_index=True)),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                (
                    "history_type",
                    models.CharField(
                        choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")],
                        max_length=1,
                    ),
                ),
                (
                    "account_manager",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="account_managers.accountmanager",
                    ),
                ),
                (
                    "client",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="clients.client",
                    ),
                ),
                (
                    "client_manager",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="client_managers.clientmanager",
                    ),
                ),
                (
                    "history_user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "supplier",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="utilities.supplier",
                    ),
                ),
                (
                    "utility",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="utilities.utility",
                    ),
                ),
            ],
            options={
                "verbose_name": "historical Client Contract",
                "verbose_name_plural": "historical Client Contracts",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": ("history_date", "history_id"),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name="Contract",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("seamless", models.BooleanField(default=False)),
                ("non_seamless", models.BooleanField(default=False)),
                (
                    "dwellent_id",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("bid_id", models.CharField(blank=True, max_length=100, null=True)),
                ("portal_status", models.URLField(blank=True, null=True)),
                ("is_directors_approval", models.BooleanField(default=False)),
                ("business_name", models.CharField(max_length=255)),
                (
                    "company_reg_number",
                    models.CharField(blank=True, max_length=20, null=True),
                ),
                ("top_line", models.CharField(max_length=30)),
                ("mpan_mpr", models.CharField(max_length=255)),
                (
                    "meter_serial_number",
                    models.CharField(blank=True, max_length=30, null=True),
                ),
                (
                    "building_name",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("site_address", models.CharField(max_length=255)),
                (
                    "billing_address",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "account_number",
                    models.CharField(blank=True, max_length=30, null=True),
                ),
                ("contract_start_date", models.DateField(blank=True, null=True)),
                ("contract_end_date", models.DateField(blank=True, null=True)),
                (
                    "contract_duration_months",
                    models.IntegerField(blank=True, null=True),
                ),
                ("is_ooc", models.BooleanField(default=False)),
                ("eac", models.CharField(max_length=30)),
                (
                    "day_consumption",
                    models.CharField(blank=True, max_length=30, null=True),
                ),
                (
                    "night_consumption",
                    models.CharField(blank=True, max_length=30, null=True),
                ),
                ("profile", models.CharField(blank=True, max_length=30, null=True)),
                (
                    "service_type",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                (
                    "feed_in_tariff",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                ("pence_per_kilowatt", models.IntegerField(blank=True, null=True)),
                (
                    "day_kilowatt_hour_rate",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                ("night_rate", models.CharField(blank=True, max_length=30, null=True)),
                (
                    "standard_charge_monthly",
                    models.CharField(blank=True, max_length=30, null=True),
                ),
                (
                    "annualised_budget",
                    models.CharField(blank=True, max_length=30, null=True),
                ),
                (
                    "commission_per_annum",
                    models.CharField(blank=True, max_length=30, null=True),
                ),
                (
                    "commission_per_unit",
                    models.CharField(blank=True, max_length=30, null=True),
                ),
                (
                    "total_commission_per_contract",
                    models.CharField(blank=True, max_length=30, null=True),
                ),
                (
                    "partner_commission",
                    models.CharField(blank=True, max_length=30, null=True),
                ),
                ("vat", models.CharField(blank=True, max_length=10, null=True)),
                (
                    "contract_value",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                (
                    "standing_charge",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                (
                    "service_charge_frequency",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "unit_rate_1",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "unit_rate_2",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "unit_rate_3",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "unit_rate_4",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "seamless_status",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "smart_meter",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("notes", models.TextField(blank=True, null=True)),
                (
                    "account_manager",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="account_manager_contracts",
                        to="account_managers.accountmanager",
                    ),
                ),
                (
                    "client",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="client_contracts",
                        to="clients.client",
                    ),
                ),
                (
                    "client_manager",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="client_manager_contracts",
                        to="client_managers.clientmanager",
                    ),
                ),
                (
                    "supplier",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="contract_suppliers",
                        to="utilities.supplier",
                    ),
                ),
                (
                    "utility",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="contract_utilities",
                        to="utilities.utility",
                    ),
                ),
            ],
            options={
                "verbose_name": "Client Contract",
                "verbose_name_plural": "Client Contracts",
                "ordering": ["contract_end_date"],
            },
        ),
        migrations.AddIndex(
            model_name="contract",
            index=models.Index(
                fields=["mpan_mpr"], name="contracts_c_mpan_mp_da9aba_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="contract",
            index=models.Index(
                fields=["client"], name="contracts_c_client__6ebd28_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="contract",
            index=models.Index(
                fields=["-client"], name="contracts_c_client__674057_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="contract",
            index=models.Index(
                fields=["business_name"], name="contracts_c_busines_c18f20_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="contract",
            index=models.Index(
                fields=["-business_name"], name="contracts_c_busines_ecb3ac_idx"
            ),
        ),
        migrations.AddConstraint(
            model_name="contract",
            constraint=models.UniqueConstraint(
                fields=("mpan_mpr", "id"), name="unique_contract"
            ),
        ),
    ]