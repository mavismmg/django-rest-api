from django.contrib import admin
from django.urls import path, include
from tvshow.views import TvshowViewSet, CastViewSet, EpisodeViewSet, SinopseViewSet, ListEpisodeTvshow
from rest_framework import routers

router = routers.DefaultRouter()
router.register('tvshow', TvshowViewSet, basename='Tvshows')
router.register('cast', CastViewSet, basename='Cast')
router.register('episode', EpisodeViewSet, basename='Episode')
router.register('sinopse', SinopseViewSet, basename='Sinopse')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('tvshow/<int:pk>/episode/', ListEpisodeTvshow.as_view())
]
