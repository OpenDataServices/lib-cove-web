# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-22 13:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("input", "0007_supplied_data_schema_version"),
    ]

    operations = [
        migrations.AddField(
            model_name="supplieddata",
            name="data_schema_version",
            field=models.CharField(default="", max_length=10),
        ),
    ]
