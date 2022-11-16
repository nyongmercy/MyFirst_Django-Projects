# basic URL Configurations
from django.urls import URLPattern, path
# import routers
from rest_framework.routers import DefaultRouter

# import everything from views
from .views import *

# define the router
router = DefaultRouter()

# define the router path and viewset to be used
router.register(r'artiste', ArtisteViewSet, basename='artiste')
router.register(r'song', SongViewSet, basename='song')
router.register(r'lyric', LyricViewSet, basename='lyric')

urlpatterns = [] + router.urls

# 127.0.0.1:8000/artiste

