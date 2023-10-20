# Generated by Django 3.2.21 on 2023-10-20 13:41

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="ProcessedPurchaseFiles",
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
                ("file_name", models.CharField(max_length=255)),
                ("processed_on", models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name="PurchaseBasket",
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
                ("purchase_date", models.DateTimeField()),
                ("cashier", models.IntegerField()),
                ("purchase_counter", models.IntegerField()),
                ("gross_amount", models.FloatField()),
                ("first_net_amount", models.FloatField()),
                ("second_net_amount", models.FloatField()),
                ("discount", models.FloatField()),
                (
                    "source_file",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="statistics.processedpurchasefiles",
                    ),
                ),
                (
                    "tapir_user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
