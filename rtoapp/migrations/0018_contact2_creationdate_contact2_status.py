# Generated by Django 4.0.2 on 2023-01-07 14:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('rtoapp', '0017_contact2'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact2',
            name='creationdate',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact2',
            name='status',
            field=models.CharField(blank=True, default='unread', max_length=200, null=True),
        ),
    ]
