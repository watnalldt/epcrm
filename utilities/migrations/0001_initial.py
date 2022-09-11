# Generated by Django 4.1.1 on 2022-09-11 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Supplier",
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
                ("supplier", models.CharField(max_length=100, unique=True)),
            ],
            options={
                "verbose_name": "Supplier",
                "verbose_name_plural": "Suppliers",
            },
        ),
        migrations.CreateModel(
            name="Utility",
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
                ("utility", models.CharField(max_length=25, unique=True)),
            ],
            options={
                "verbose_name": "Utility",
                "verbose_name_plural": "Utilities",
            },
        ),
    ]