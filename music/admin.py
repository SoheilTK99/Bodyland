from django.contrib import admin
from .models import Music


admin.site.register(Music)

# @admin.register(Music)
# class MusicAdmin(admin.ModelAdmin):
#     list_display = ('music_name','aartist_nameuthor','categorey',)

