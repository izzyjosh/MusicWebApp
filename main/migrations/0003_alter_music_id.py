# Generated by Django 4.2.7 on 2023-12-17 23:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0002_auto_20231212_2300"),
    ]

    operations = [
        migrations.AlterField(
            model_name="music",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
