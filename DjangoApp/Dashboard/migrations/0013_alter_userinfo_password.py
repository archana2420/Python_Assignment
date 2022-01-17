# Generated by Django 3.2.11 on 2022-01-17 09:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0012_alter_userinfo_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='password',
            field=models.CharField(max_length=100, validators=[django.core.validators.RegexValidator(message='Password must be of 8 characters(only alphabets and anumbers allowed)', regex='[a-zA-Z0-9]{8}$')]),
        ),
    ]
