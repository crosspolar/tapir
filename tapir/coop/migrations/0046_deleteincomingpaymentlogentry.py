# Generated by Django 3.2.25 on 2024-08-05 15:13

import django.contrib.postgres.fields.hstore
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("log", "0007_auto_20240702_1748"),
        ("coop", "0045_updateincomingpaymentlogentry"),
    ]

    operations = [
        migrations.CreateModel(
            name="DeleteIncomingPaymentLogEntry",
            fields=[
                (
                    "logentry_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="log.logentry",
                    ),
                ),
                ("values", django.contrib.postgres.fields.hstore.HStoreField()),
            ],
            options={
                "abstract": False,
            },
            bases=("log.logentry",),
        ),
    ]