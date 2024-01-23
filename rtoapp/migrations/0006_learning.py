# Generated by Django 4.1.2 on 2023-01-05 08:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("rtoapp", "0005_registration"),
    ]

    operations = [
        migrations.CreateModel(
            name="Learning",
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
                (
                    "learningnumber",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("father", models.CharField(blank=True, max_length=100, null=True)),
                ("birth", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "qualification",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "licencetype",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("blood", models.CharField(blank=True, max_length=100, null=True)),
                ("peraddress", models.CharField(blank=True, max_length=100, null=True)),
                ("comaddress", models.CharField(blank=True, max_length=100, null=True)),
                ("image2", models.FileField(blank=True, null=True, upload_to="")),
                ("creationdate", models.DateTimeField(auto_now_add=True)),
                (
                    "city",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="rtoapp.city",
                    ),
                ),
                (
                    "state",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="rtoapp.state",
                    ),
                ),
            ],
        ),
    ]