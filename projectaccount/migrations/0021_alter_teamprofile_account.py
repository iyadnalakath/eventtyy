# Generated by Django 4.1.6 on 2023-03-28 07:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("projectaccount", "0020_teamprofile"),
    ]

    operations = [
        migrations.AlterField(
            model_name="teamprofile",
            name="account",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="team_profile",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
