# Generated by Django 3.2.20 on 2023-07-10 04:00

import cove.input.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('input', '0009_supplieddata_parameters'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplieddata',
            name='original_file',
            field=models.FileField(max_length=256, upload_to=cove.input.models.upload_to),
        ),
    ]
