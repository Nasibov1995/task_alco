# Generated by Django 4.2.2 on 2024-03-29 22:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0003_blockedip"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="ip_address",
            field=models.GenericIPAddressField(default=0),
            preserve_default=False,
        ),
    ]
