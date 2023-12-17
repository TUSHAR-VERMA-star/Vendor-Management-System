# Generated by Django 4.2.5 on 2023-12-14 07:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Vendor",
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
                ("name", models.CharField(max_length=255)),
                ("contact_details", models.TextField()),
                ("address", models.TextField()),
                ("vendor_code", models.CharField(max_length=50, unique=True)),
                ("on_time_delivery_rate", models.FloatField(blank=True, null=True)),
                ("quality_rating_avg", models.FloatField(blank=True, null=True)),
                ("average_response_time", models.FloatField(blank=True, null=True)),
                ("fulfillment_rate", models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="PurchaseOrder",
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
                ("po_number", models.CharField(max_length=50, unique=True)),
                ("order_date", models.DateTimeField()),
                ("delivery_date", models.DateTimeField()),
                ("items", models.JSONField()),
                ("quantity", models.IntegerField()),
                ("status", models.CharField(max_length=50)),
                ("quality_rating", models.FloatField(blank=True, null=True)),
                ("issue_date", models.DateTimeField()),
                ("acknowledgment_date", models.DateTimeField(blank=True, null=True)),
                (
                    "vendor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.vendor"
                    ),
                ),
            ],
        ),
    ]
