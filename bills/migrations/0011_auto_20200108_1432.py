# Generated by Django 3.0.2 on 2020-01-08 13:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("bills", "0010_auto_20200108_1430"),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="user",
            field=models.ForeignKey(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="events",
                to=settings.AUTH_USER_MODEL,
            ),
        )
    ]
