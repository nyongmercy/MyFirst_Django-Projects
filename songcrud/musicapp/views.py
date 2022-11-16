# import viewsets
from rest_framework import viewsets

# import local data
from .models import Artiste, Song, Lyric
from .serializers import ArtisteSerializer, SongSerializer, LyricSerializer

# create a viewset
class ArtisteViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = Artiste.objects.all()

    # specify serializer to be used
    serializer_class = ArtisteSerializer

    # create a viewset
class SongViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = Song.objects.all()

    # specify serializer to be used
    serializer_class = SongSerializer

    # create a viewset
class LyricViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = Lyric.objects.all()

    # specify serializer to be used
    serializer_class = LyricSerializer
    


# trying out sto remember
"""
payload = (
    "first_name": "Okon",
    "last_name": "Edem",
    "age": 56
)

Artiste.objects.create(first_name=payload('first_name'),)

"""
