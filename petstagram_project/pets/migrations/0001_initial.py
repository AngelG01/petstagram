# Generated by Django 5.1.1 on 2024-10-09 12:34

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Pets",
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
                ("name", models.CharField(max_length=30)),
                ("professional_pet_photo", models.URLField()),
                ("date_of_birth", models.DateField(blank=True, null=True)),
                ("slug", models.SlugField(unique=True)),
            ],
        ),
    ]