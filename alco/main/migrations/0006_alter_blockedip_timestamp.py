# Generated by Django 4.2.2 on 2024-03-30 09:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0005_alter_customuser_ip_address"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blockedip",
            name="timestamp",
            field=models.DateTimeField(auto_now_add=True, db_index=True),
        ),
    ]
