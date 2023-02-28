# Generated by Django 4.1.7 on 2023-02-28 11:49

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Tasklist",
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
                ("text", models.CharField(help_text="Задача", max_length=100)),
                ("is_done", models.BooleanField(default=False, help_text="Выполнена")),
                (
                    "timestamp_create",
                    models.DateTimeField(
                        auto_now_add=True, help_text="Когда создана", null=True
                    ),
                ),
                (
                    "timestamp_done",
                    models.DateTimeField(
                        blank=True, help_text="Когда выполнена", null=True
                    ),
                ),
            ],
        ),
    ]
