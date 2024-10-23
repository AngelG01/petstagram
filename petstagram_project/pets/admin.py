from django.contrib import admin

from petstagram_project.pets.models import Pet


# Register your models here.
@admin.register(Pet)
class PetsAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')