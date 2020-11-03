from django.contrib import admin
from .models import Song

# Register your models here.
class SongAdmin(admin.ModelAdmin):
    list_display = ['name', 'songid', 'artist', 'language', 'category' ]
    search_fields = ['name', 'songid', 'artist', 'language', 'category' ]
    class Meta:
        model = Song

admin.site.register(Song, SongAdmin)