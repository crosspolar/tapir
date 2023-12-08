# Generated by Django 3.2.23 on 2023-11-16 10:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("shifts", "0052_solidarityshift"),
    ]

    operations = [
        migrations.AddField(
            model_name="solidarityshift",
            name="date_gifted",
            field=models.DateField(
                auto_now_add=True,
                default=datetime.datetime(2023, 11, 16, 11, 30, 14, 216680),
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="solidarityshift",
            name="date_used",
            field=models.DateField(null=True),
        ),
    ]