# Generated by Django 5.1.1 on 2024-10-12 13:24

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("pets", "0003_alter_pet_slug"),
    ]

    operations = [
        migrations.RenameField(
            model_name="pet",
            old_name="professional_pet_photo",
            new_name="personal_photo",
        ),
    ]