from rest_framework import viewsets, generics
from tvshow.models import Tvshow, Cast, EpisodeReleaseDate, Sinopse
from tvshow.serializer import TvshowSerializer, CastSerializer, EpisodeSerializer, SinopseSerializer, ListTvshowEpisodeSerializer

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

class ListEpisodeTvshow(generics.ListAPIView):
    """List episode release per day for Tvshow"""
    def get_queryset(self):
        queryset = EpisodeReleaseDate.objects.filter(tvshow_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListTvshowEpisodeSerializer