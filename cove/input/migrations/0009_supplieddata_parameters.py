# Generated by Django 2.2.16 on 2022-06-06 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('input', '0008_supplieddata_data_schema_version'),
    ]

    operations = [
        migrations.AddField(
            model_name='supplieddata',
            name='parameters',
            field=models.TextField(blank=True, null=True),
        ),
    ]
