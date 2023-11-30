from django.contrib import admin
from .models import Music

@admin.register(Music)
class MusicAdmin(admin.ModelAdmin):
    list_display = ("title","music_file","musician")

