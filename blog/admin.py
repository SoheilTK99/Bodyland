from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','author','status','published_at',)
    list_filter = ('status',)
    search_fields = ('title','body',)
    date_hierarchy = ('published_at')
    list_editable = ('status',)
