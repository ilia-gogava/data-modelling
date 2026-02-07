from django.contrib import admin
from .models import Genre, Artist, Album, Track, AudioFeatures

admin.site.register(Genre)
admin.site.register(Artist)
admin.site.register(Album)
admin.site.register(Track)
admin.site.register(AudioFeatures)
