from django.db import models
from django.utils.timezone import now

class Tvshow(models.Model):
    name = models.CharField(max_length=30)
    launch_date = models.DateField()
    autor = models.CharField(max_length=30)
    genre = models.CharField(max_length=512)
    producer = models.CharField(max_length=20)
    creators = models.CharField(max_length=512)
    language = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Cast(models.Model):
    OTHERS = (
        ('T', 'Tvshow'),
        ('M', 'Movies')
    )
    cast = models.CharField(max_length=512)
    related_tvshows = models.CharField(max_length=1, choices=OTHERS, blank=False, null=False, default='T')

    def __str__(self):
        return self.cast

class Sinopse(models.Model):
    sinopse = models.ForeignKey(Tvshow, on_delete=models.CASCADE)
    text = models.CharField(max_length=1024, default='no sinopse provided')

class EpisodeReleaseDate(models.Model):
    TIME_PERIOD = (
        ('M', 'Morning'),
        ('A', 'Afternoon'),
        ('N', 'Night')
    )
    tvshow = models.ForeignKey(Tvshow, on_delete=models.CASCADE)
    day = models.CharField(max_length=15, default='')
    daytime = models.DateTimeField(default=now)
    time_period = models.CharField(max_length=1, choices=TIME_PERIOD, blank=False, default='A')