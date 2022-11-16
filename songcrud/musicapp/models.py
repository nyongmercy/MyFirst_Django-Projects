from turtle import title
from unittest.util import _MAX_LENGTH
from django.db import models
from datetime import datetime

# Create your models here.

class Artiste(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    age = models.IntegerField()

    def __str__(self):
          return self.first_name

class Song(models.Model):
    title = models.CharField(max_length=100)
    date_released = models.DateField()
    likes = models.PositiveIntegerField(default=0)
    artiste_id = models.ForeignKey(Artiste, related_name='artiste_id', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title                         
class Lyric(models.Model):
    content = models.TextField()
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE) 

