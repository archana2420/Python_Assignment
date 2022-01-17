# Generated by Django 3.2.11 on 2022-01-17 09:32

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0003_alter_userinfo_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='phone_number',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(message='Phone number must be 10 digits', regex='\\d{10}$')]),
        ),
    ]
