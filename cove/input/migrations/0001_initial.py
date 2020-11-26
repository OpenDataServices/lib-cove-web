# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="SuppliedData",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        serialize=False,
                        editable=False,
                        primary_key=True,
                        default=uuid.uuid4,
                    ),
                ),
                ("source_url", models.URLField(null=True)),
                ("original_file", models.FileField(upload_to="")),
            ],
        ),
    ]
