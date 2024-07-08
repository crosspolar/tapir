# Generated by Django 3.2.25 on 2024-07-07 20:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shifts', '0056_shiftaccountentry_is_solidarity_used'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShiftNotification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notification_timedelta', models.DurationField()),
                ('shift_to_be_notified_about', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shifts.shift')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shift_notification_entry', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddConstraint(
            model_name='shiftnotification',
            constraint=models.UniqueConstraint(fields=('user', 'shift_to_be_notified_about'), name='user_shift_constraint'),
        ),
    ]
