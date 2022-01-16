# Generated by Django 3.2.6 on 2022-01-16 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('dob', models.DateField(verbose_name='Date of birth')),
                ('phone_number', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]
