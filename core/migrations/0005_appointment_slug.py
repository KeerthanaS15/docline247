# Generated by Django 3.2.5 on 2022-02-26 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20220215_1245'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, null=True),
        ),
    ]