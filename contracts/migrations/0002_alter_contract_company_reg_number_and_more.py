# Generated by Django 4.1.1 on 2022-09-11 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("contracts", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contract",
            name="company_reg_number",
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name="historicalcontract",
            name="company_reg_number",
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]