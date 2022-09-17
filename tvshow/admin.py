from django.contrib import admin
from tvshow.models import Tvshow, Cast, EpisodeReleaseDate, Sinopse

class Tvshows(admin.ModelAdmin):
    list_display = ('id', 'name', 'launch_date', 'autor', 'genre', 'producer', 'creators', 'language')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 20

admin.site.register(Tvshow, Tvshows)

class CastMembers(admin.ModelAdmin):
    list_display = ('id', 'cast', 'related_tvshows')
    list_display_links = ('id', 'cast')
    search_fields = ('cast', )

admin.site.register(Cast, CastMembers)

class SinopseShow(admin.ModelAdmin):
    list_display = ('id', 'sinopse')
    list_display_links = ('id', )

admin.site.register(Sinopse, SinopseShow)

class EpisodeReleaseDay(admin.ModelAdmin):
    list_display = ('id', 'tvshow', 'day', 'daytime', 'time_period')
    list_display_links = ('id', )

admin.site.register(EpisodeReleaseDate, EpisodeReleaseDay)