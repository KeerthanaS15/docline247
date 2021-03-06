# Generated by Django 3.2.5 on 2022-02-15 12:45

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_create_doctors'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AlterField(
            model_name='category',
            name='icon',
            field=models.ImageField(upload_to='categories/'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='profile_pic',
            field=models.ImageField(upload_to='doctors/'),
        ),
    ]
