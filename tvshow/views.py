from rest_framework import viewsets, generics
from tvshow.models import User, Tvshow, Cast, Sinopse, EpisodeReleaseDate, Episode, Watching
from tvshow.serializer import UserSerializer, TvshowSerializer, CastSerializer, SinopseSerializer, EpisodeReleaseDataSerializer, EpisodeSerializer, WatchingSerializer, ListTvshowEpisodeSerializer, ListTvshowsByCastSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class UserViewSet(viewsets.ModelViewSet):
  """Register user"""
  queryset = User.objects.all()
  serializer_class = UserSerializer

class TvshowViewSet(viewsets.ModelViewSet):
  """Show all registred Tvshows"""
  queryset = Tvshow.objects.all()
  serializer_class = TvshowSerializer
  authentication_classes = [BasicAuthentication]
  permission_classes = [IsAuthenticated]

class CastViewSet(viewsets.ModelViewSet):
  """Show all members from Cast"""
  queryset = Cast.objects.all()
  serializer_class = CastSerializer
  authentication_classes = [BasicAuthentication]
  permission_classes = [IsAuthenticated]

class SinopseViewSet(viewsets.ModelViewSet):
  """Show tvshow/movie sinopse"""
  queryset = Sinopse.objects.all()
  serializer_class = SinopseSerializer
  authentication_classes = [BasicAuthentication]
  permission_classes = [IsAuthenticated]

class EpisodeReleaseDateViewSet(viewsets.ModelViewSet):
  """Show episode release day"""
  queryset = EpisodeReleaseDate.objects.all()
  serializer_class = EpisodeReleaseDataSerializer

class EpisodeViewSet(viewsets.ModelViewSet):
  """Show list of eps"""
  queryset = Episode.objects.all()
  serializer_class = EpisodeSerializer

class WatchingViewSet(viewsets.ModelViewSet):
  """Set watching eps"""
  queryset = Watching.objects.all()
  serializer_class = WatchingSerializer

class ListEpisodeTvshow(generics.ListAPIView):
  """List episode release per day for Tvshow"""
  def get_queryset(self):
    queryset = EpisodeReleaseDate.objects.filter(tvshow_id=self.kwargs['pk'])
    return queryset
  serializer_class = ListTvshowEpisodeSerializer

class ListTvshowByCast(generics.ListAPIView):
  """List tvshow by cast members"""
  def get_queryset(self):
    queryset = Cast.objects.filter(cast_id=self.kwargs['pk'])
    return queryset
  serializer_class = ListTvshowsByCastSerializer