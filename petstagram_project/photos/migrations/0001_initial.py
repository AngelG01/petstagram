# Generated by Django 5.1.1 on 2024-10-09 14:52

import django.core.validators
import petstagram_project.photos.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("pets", "0003_alter_pet_slug"),
    ]

    operations = [
        migrations.CreateModel(
            name="Photo",
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
                    "photo",
                    models.ImageField(
                        upload_to="",
                        validators=[
                            petstagram_project.photos.validators.validate_photo_size
                        ],
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        max_length=300,
                        null=True,
                        validators=[django.core.validators.MinLengthValidator(10)],
                    ),
                ),
                ("location", models.CharField(blank=True, max_length=30, null=True)),
                ("date_of_publication", models.DateField(auto_now=True)),
                ("tagged_pets", models.ManyToManyField(blank=True, to="pets.pet")),
            ],
        ),
    ]
