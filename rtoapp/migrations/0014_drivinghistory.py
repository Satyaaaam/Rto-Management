# Generated by Django 4.1.2 on 2023-01-06 09:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("rtoapp", "0013_alter_trackinghistory_status"),
    ]

    operations = [
        migrations.CreateModel(
            name="Drivinghistory",
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
                ("remark", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "status",
                    models.CharField(
                        blank=True, default="Not Updated Yet", max_length=100, null=True
                    ),
                ),
                ("time", models.DateTimeField(auto_now_add=True)),
                (
                    "driving",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="rtoapp.driving",
                    ),
                ),
            ],
        ),
    ]
