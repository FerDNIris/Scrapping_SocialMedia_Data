# Generated by Django 5.2 on 2025-04-16 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="RespuestaGemini",
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
                ("pregunta", models.TextField()),
                ("respuesta", models.TextField()),
                ("fecha_respuesta", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
