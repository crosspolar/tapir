# Generated by Django 3.2.23 on 2023-11-28 14:58

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("shifts", "0054_shiftaccountentry_is_solidarity_entry"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="shiftaccountentry",
            name="is_solidarity_entry",
        ),
    ]