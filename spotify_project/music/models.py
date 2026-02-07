from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    
class Artist(models.Model):
    name = models.CharField(max_length=255)
    popularity = models.PositiveIntegerField()
    followers = models.PositiveIntegerField()
    genres = models.ManyToManyField(Genre, related_name="artists")

    def __str__(self):
        return self.name
    
class Album(models.Model):
    name = models.CharField(max_length=255)
    artist = models.ForeignKey(
        Artist,
        on_delete=models.CASCADE,
        related_name="albums"
    )
    release_date = models.DateField()
    total_tracks = models.PositiveIntegerField()

    ALBUM_TYPES = (
        ("album", "Album"),
        ("single", "Single"),
        ("compilation", "Compilation"),
    )
    album_type = models.CharField(max_length=20, choices=ALBUM_TYPES)

    def __str__(self):
        return f"{self.name} - {self.artist.name}"

class Track(models.Model):
    name = models.CharField(max_length=255)
    album = models.ForeignKey(
        Album,
        on_delete=models.CASCADE,
        related_name="tracks"
    )
    artists = models.ManyToManyField(Artist, related_name="tracks")
    duration_ms = models.PositiveIntegerField()
    explicit = models.BooleanField(default=False)
    popularity = models.PositiveIntegerField()
    track_number = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class AudioFeatures(models.Model):
    track = models.OneToOneField(
        Track,
        on_delete=models.CASCADE,
        related_name="audio_features"
    )
    danceability = models.FloatField()
    energy = models.FloatField()
    loudness = models.FloatField()
    speechiness = models.FloatField()
    acousticness = models.FloatField()
    instrumentalness = models.FloatField()
    liveness = models.FloatField()
    valence = models.FloatField()
    tempo = models.FloatField()

    def __str__(self):
        return f"Audio Features - {self.track.name}"
