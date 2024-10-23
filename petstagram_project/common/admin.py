from django.contrib import admin

from petstagram_project.common.models import Comment
from petstagram_project.pets.models import Pet


# Register your models here.
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'date_time_of_publication')
