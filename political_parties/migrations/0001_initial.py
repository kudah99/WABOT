# Generated by Django 4.2.2 on 2023-06-27 17:37

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Political_Parties",
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
                ("name", models.CharField(max_length=50)),
                ("logo", models.URLField(max_length=100)),
                ("statement", models.CharField(max_length=300)),
            ],
        ),
    ]
