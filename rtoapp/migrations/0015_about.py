# Generated by Django 4.1.2 on 2023-01-07 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rtoapp", "0014_drivinghistory"),
    ]

    operations = [
        migrations.CreateModel(
            name="About",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("pagetitle", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "description",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
            ],
        ),
    ]
