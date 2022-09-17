from rest_framework import viewsets
from tvshow.models import Tvshow, Cast, EpisodeReleaseDate, Sinopse
from tvshow.serializer import TvshowSerializer, CastSerializer, EpisodeSerializer, SinopseSerializer

class TvshowViewSet(viewsets.ModelViewSet):
    """Show all registred Tvshows"""
    queryset = Tvshow.objects.all()
    serializer_class = TvshowSerializer

class CastViewSet(viewsets.ModelViewSet):
    """Show all members from Cast"""
    queryset = Cast.objects.all()
    serializer_class = CastSerializer

class SinopseViewSet(viewsets.ModelViewSet):
    """Show tvshow/movie sinopse"""
    queryset = Sinopse.objects.all()
    serializer_class = SinopseSerializer

class EpisodeViewSet(viewsets.ModelViewSet):
    """Show episode release day"""
    queryset = EpisodeReleaseDate.objects.all()
    serializer_class = EpisodeSerializer