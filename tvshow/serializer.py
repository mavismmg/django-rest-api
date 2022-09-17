from dataclasses import fields
from msilib.schema import Class
from pyexpat import model
from rest_framework import serializers
from tvshow.models import Tvshow, Cast, EpisodeReleaseDate, Sinopse

class TvshowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tvshow
        fields = ['id', 'name', 'launch_date', 'autor', 'genre', 'producer', 'creators', 'language']

class CastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cast
        fields = '__all__'

class SinopseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sinopse
        fields = ['id', 'text']

class EpisodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EpisodeReleaseDate
        exclude = []

class ListTvshowEpisodeSerializer(serializers.ModelSerializer):
    name = serializers.ReadOnlyField(source='tvshow.name')
    sinopse = serializers.ReadOnlyField(source='sinopse.genre')
    time_period = serializers.SerializerMethodField()
    class Meta:
        model = EpisodeReleaseDate
        fields = ['name', 'sinopse', 'day', 'daytime', 'time_period']
    def get_time_period(self, timeperiodObj):
        return timeperiodObj.get_time_period_display()