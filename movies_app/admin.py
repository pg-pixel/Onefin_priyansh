from django.contrib import admin
from .models import Collection, Movie, GenreCount
# Register your models here.

@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'description')

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'genres', 'display_collections')

    def display_collections(self, obj):
        return ", ".join([collection.title for collection in obj.collection.all()])
    
    display_collections.short_description = 'Collections'

@admin.register(GenreCount)
class GenreCountAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'genre_name', 'genre_count')