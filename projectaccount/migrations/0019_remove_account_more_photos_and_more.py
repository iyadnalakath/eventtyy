# Generated by Django 4.1.6 on 2023-02-17 11:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projectaccount', '0018_account_more_photos_account_profile_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='more_photos',
        ),
        migrations.RemoveField(
            model_name='account',
            name='profile_pic',
        ),
    ]