# Generated by Django 4.1.6 on 2023-02-27 06:35

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0056_remove_service_amount"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="profilepic",
            name="profile_pic",
        ),
    ]
