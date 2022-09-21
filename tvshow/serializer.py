from rest_framework import serializers
from tvshow.models import User, Tvshow, Cast, Sinopse, EpisodeReleaseDate, Episode, Watching
from tvshow.validators import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
    def validate(self, data):
        if not validate_username(data['username']):
            raise serializers.ValidationError({
                'username':
                data['username'] + 
                ' is an invalid username, should contain 6 to 30 characters and should not contain invalid characters.'
                })
        e = EmailCheck()
        if not e.validate_email(data['email']):
            raise serializers.ValidationError({
                'email':
                'Invalid email. ' +
                e.message
            })
        p = PasswordCheck()
        if not p.validate_password(data['password']):
            raise serializers.ValidationError({
                'password':
                'Invalid password. ' + 
                p.message
            })
        return data

class TvshowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tvshow
        fields = '__all__'
    def validate(self, data):
        if not validate_tvshow_autor(data['autor']):
            raise serializers.ValidationError({
                'autor':
                data['autor'] +
                ' , autor name should have capital letters. Example: John.'
            })
        if not validate_tvshow_genre(data['genre']):
            raise serializers.ValidationError({
                'genre':
                data['autor'] + 
                ' , informat is incorrect. Should contain more than one genre.'
            })
        if not validate_tvshow_language(data['language']):
            raise serializers.ValidationError({
                'language':
                data['language'] + 
                ' , should contain only letters and one capital letter in it..'
            })
        return data

class CastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cast
        fields = '__all__'
    def validate(self, data):
        c = CastCheck()
        if not c.validate_cast_members(data['cast_members']):
            raise serializers.ValidationError({
                'cast_members':
                data['cast_members'] + 
                ' , should contain more than one member.'
            })
        return data

class SinopseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sinopse
        fields = ['id', 'sinopse_desc']

class EpisodeReleaseDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = EpisodeReleaseDate
        exclude = []

class EpisodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Episode
        fields = '__all__'

class WatchingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Watching
        fields = '__all__'

class ListTvshowEpisodeSerializer(serializers.ModelSerializer):
    name = serializers.ReadOnlyField(source='tvshow.name')
    sinopse = serializers.ReadOnlyField(source='sinopse.genre')
    time_period = serializers.SerializerMethodField()
    class Meta:
        model = EpisodeReleaseDate
        fields = ['name', 'sinopse', 'day', 'daytime', 'time_period']
    def get_time_period(self, timeperiodObj):
        return timeperiodObj.get_time_period_display()

class ListTvshowsByCastSerializer(serializers.ModelSerializer):
    tvshow_name = serializers.ReadOnlyField(source='cast.name')
    class Meta:
        model = Cast
        fields = ['tvshow_name', 'cast_members']