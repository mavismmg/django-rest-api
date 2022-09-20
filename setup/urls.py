from django.contrib import admin
from django.urls import path, include
from tvshow.views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('tvshow', TvshowViewSet, basename='Tvshows')
router.register('cast', CastViewSet, basename='Cast')
router.register('episode_date', EpisodeReleaseDateViewSet, basename='EpisodeDate')
router.register('sinopse', SinopseViewSet, basename='Sinopse')
router.register('user', UserViewSet, basename='User')
router.register('episode', EpisodeViewSet, basename='Episode')
router.register('watching', WatchingViewSet, basename='Watching')

urlpatterns = [
  path('admin/', admin.site.urls),
  path('', include(router.urls)),
  path('tvshow/<int:pk>/episode/', ListEpisodeTvshow.as_view()),
  path('cast/<int:pk>/tvshows/', ListTvshowByCast.as_view())
]
