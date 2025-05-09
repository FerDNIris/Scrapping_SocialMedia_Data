# Generated by Django 5.2 on 2025-04-21 23:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("scraping", "0004_alter_tweet_created_at"),
    ]

    operations = [
        migrations.CreateModel(
            name="ResultadoAnalisisSentimiento",
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
                ("texto_analizado", models.TextField()),
                ("sentimiento", models.CharField(max_length=50)),
                ("score", models.FloatField(blank=True, null=True)),
                ("fecha_analisis", models.DateTimeField(auto_now_add=True)),
                (
                    "tweet",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="analisis_sentimientos",
                        to="scraping.tweet",
                    ),
                ),
            ],
        ),
    ]
