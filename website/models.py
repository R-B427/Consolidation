from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

class Album(models.Model):
    """
    Model representing an album.
    Attributes:
        title (str): The title of the album.
        artist (str): The artist of the album.
        release_date (datetime): The release date of the album.
        genre (str): The genre of the album.
    """
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    release_date = models.DateField()
    genre = models.CharField(max_length=50)

    def __str__(self):
        return str(self.title)


User.add_to_class('favorite_albums', models.ManyToManyField(Album, blank=True, related_name='favorited_by'))


class Event(models.Model):
    """
    Model representing an event.
    Attributes:
        title (str): The title of the event.
        date (datetime): The date and time of the event.
        venue (str): The venue where the event will take place.
        description (str): A description of the event.
    """
    title = models.CharField(max_length=100)
    date = models.DateTimeField()
    venue = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return str(self.title)

# Create your models here.
