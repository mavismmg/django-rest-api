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
        fields = '__all__'

class EpisodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EpisodeReleaseDate
        exclude = []