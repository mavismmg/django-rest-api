from django.db import models
from django.utils.timezone import now

class User(models.Model):
    username = models.CharField(max_length=12, unique=True, null=False)
    email = models.EmailField(blank=False, max_length=30, null=False)
    password = models.CharField(max_length=30, null=False, default='')

    def __str__(self):
        return self.username

class Tvshow(models.Model):
    name = models.CharField(max_length=512)
    autor = models.CharField(max_length=256)
    genre = models.CharField(max_length=1024)
    producer = models.CharField(max_length=512)
    creators = models.CharField(max_length=256)
    language = models.CharField(max_length=256)
    launch_date = models.DateField()
    full_launch = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Cast(models.Model):
    OTHERS = (
        ('T', 'Tvshow'),
        ('M', 'Movies')
    )
    cast = models.ForeignKey(Tvshow, related_name='cast', on_delete=models.CASCADE)
    cast_members = models.CharField(max_length=512)
    related_tvshows = models.CharField(max_length=1, choices=OTHERS, blank=False)

    def __str__(self):
        return self.cast

class Sinopse(models.Model):
    sinopse = models.ForeignKey(Tvshow, on_delete=models.CASCADE)
    sinopse_desc = models.CharField(max_length=1024, default='null')

    def __str__(self):
        return self.sinopse_desc

class Episode(models.Model):
    name = models.ForeignKey(Tvshow, on_delete=models.CASCADE)
    episode = models.CharField(max_length=1)

    def __str__(self):
        return self.episode

class EpisodeReleaseDate(models.Model):
    TIME_PERIOD = (
        ('M', 'Morning'),
        ('A', 'Afternoon'),
        ('N', 'Night')
    )
    tvshow = models.ForeignKey(Tvshow, on_delete=models.CASCADE)
    day = models.CharField(max_length=16)
    daytime = models.DateTimeField(default=now)
    time_period = models.CharField(max_length=1, choices=TIME_PERIOD, blank=False, default='A')

class Watching(models.Model):
    currently_watching = models.ForeignKey(Tvshow, on_delete=models.CASCADE)
    currently_episode = models.ForeignKey(Episode, on_delete=models.CASCADE)

    def __str__(self):
        return self.currently_episode