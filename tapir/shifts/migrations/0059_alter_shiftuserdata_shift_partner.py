# Generated by Django 3.2.25 on 2024-08-27 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("shifts", "0058_alter_shiftuserdata_shift_partner"),
    ]

    operations = [
        migrations.AlterField(
            model_name="shiftuserdata",
            name="shift_partner",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="shift_partner_of",
                to="shifts.shiftuserdata",
            ),
        ),
    ]
