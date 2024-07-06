# Generated by Django 3.2.25 on 2024-07-06 13:12

import django.contrib.postgres.fields
from django.db import migrations, models
import ldapdb.models.fields
import tapir.core.tapir_email_base


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_auto_20230605_0951'),
    ]

    operations = [
        migrations.AddField(
            model_name='tapiruser',
            name='additional_mails',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=128), blank=True, default=tapir.core.tapir_email_base.mails_not_mandatory, size=None),
        ),
    ]
