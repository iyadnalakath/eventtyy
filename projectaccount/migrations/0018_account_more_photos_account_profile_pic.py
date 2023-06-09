# Generated by Django 4.1.6 on 2023-02-17 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectaccount', '0017_remove_account_more_photos_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='more_photos',
            field=models.ImageField(blank=True, default='', null=True, upload_to='mediafiles'),
        ),
        migrations.AddField(
            model_name='account',
            name='profile_pic',
            field=models.ImageField(blank=True, default='', null=True, upload_to='mediafiles'),
        ),
    ]
