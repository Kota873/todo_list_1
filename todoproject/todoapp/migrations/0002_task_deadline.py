# Generated by Django 4.2.9 on 2024-02-03 02:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("todoapp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="deadline",
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
