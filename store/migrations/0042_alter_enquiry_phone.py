# Generated by Django 4.1.6 on 2023-02-15 07:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0041_alter_enquiry_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquiry',
            name='phone',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinLengthValidator(10), django.core.validators.MaxLengthValidator(10)]),
        ),
    ]
