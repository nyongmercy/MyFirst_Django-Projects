from turtle import title
from unittest.util import _MAX_LENGTH
from django.db import models
from datetime import datetime

# Create your models here.

class Artiste(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    age = models.IntegerField()

class Song(models.Model):
    title = models.CharField(max_length=100)
    date_released = models.DateField()
    likes = models.PositiveIntegerField(default=0)
    artiste_id = models.ForeignKey(Artiste, on_delete=models.CASCADE)


class Lyric(models.Model):
    content = models.TextField()
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE) 

