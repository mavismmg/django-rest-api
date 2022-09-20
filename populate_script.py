from email.policy import default
from logging import exception
import os, django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from faker import Faker
from django.utils.timezone import now
import random
from tvshow.models import *

class Populate:
  Faker.seed(10)

  def __init__(self, fake=Faker('en_us')):
    self.fake = fake
    self.titles = []

  @staticmethod
  def execute_populate(range_):
    p = Populate()
    try:
      p.populate_users(range_)
      p.populate_tvshows(range_)
      p.populate_cast(range_)
      p.populate_sinopse(range_)
      p.populate_episode(range_)
      p.populate_episode_release_date(range_)
      p.populate_watching(range_)
      pass
    except Exception as exception:
      print('Script could not pass request validation: ', exception)
      pass

  def populate_users(self, users):
    try:
      for _ in range(users):
        username = self.fake.name()
        email = '{}@{}'.format(username.lower(), self.fake.free_email_domain())
        email = email.replace(' ', '')
        password = '{}{}'.format(random.randrange(1000, 9999), 'xyzXYZ&')
        User(username=username, email=email, password=password).save()
        pass
    except Exception as exception:
      raise exception

  def populate_tvshows(self, tvshows):
    try:
      for _ in range(tvshows):
        title = '{}{}'.format('generic_title', _)
        self.titles.append(title)
        autor = '{}{}'.format('Autor_rand', _)
        genre = '{}{}'.format('rand_genre', _)
        producer = '{}{}'.format('rand_producer', _)
        creators = '{}{}'.format('rand_creators', _)
        language = '{}{}'.format('Language_rand', _)
        launch_date = '{}-{}-{}'.format(random.randrange(2000, 2022), random.randrange(1, 12),
                                        random.randrange(1, 31))
        full_launch = random.choice([True, False])
        Tvshow(title=title, autor=autor, genre=genre, producer=producer, creators=creators,
              language=language, launch_date=launch_date, full_launch=full_launch).save()
        pass
    except Exception as exception:
      raise exception

  def populate_cast(self, casts):
    try:
      for _ in range(casts):
        id_ = Tvshow.objects.get(id='{}'.format(_ + 1))
        cast = id_
        cast_members = '{}{}, {}{}, {}{}'.format('member', random.randint(0, 99), 'member',
                                          random.randint(100, 199), 'member', random.randint(200, 299))
        related_tvshows = random.choice(['T', 'M'])
        Cast(cast=cast, cast_members=cast_members, related_tvshows=related_tvshows).save()
        pass
    except Exception as exception:
      raise exception

  def populate_sinopse(self, sinopses):
    try:
      for _ in range(sinopses):
        id_ = Tvshow.objects.get(id='{}'.format(_ + 1))
        sinopse = id_
        sinopse_desc = 'random generated sinopse text {}'.format(random.randint(0, 999))
        Sinopse(sinopse=sinopse, sinopse_desc=sinopse_desc).save()
        pass
    except Exception as exception:
      raise exception

  def populate_episode(self, episodes):
    try:
      for _ in range(episodes):
        id_ = Tvshow.objects.get(id='{}'.format(_ + 1))
        name = id_
        episode = '{}'.format(random.randrange(0, 9))
        Episode(name=name, episode=episode).save()
        pass
    except Exception as exception:
      raise exception

  def populate_episode_release_date(self, episodes):
    try:
      for _ in range(episodes):
        id_ = Tvshow.objects.get(id='{}'.format(_ + 1))
        tvshow = id_
        day = random.choice(['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'])
        daytime = now()
        time_period = random.choice(['M', 'A', 'N'])
        EpisodeReleaseDate(tvshow=tvshow, day=day, daytime=daytime, time_period=time_period).save()
        pass
    except Exception as exception:
      raise exception

  def populate_watching(self, watchings):
    try:
      for _ in range(watchings):
        print(self.titles)
        id_tv = Tvshow.objects.get(title='{}'.format(self.titles[_]))
        currently_watching = id_tv
        id_ep = Episode.objects.get(id='{}'.format(_ + 1))
        currently_episode = id_ep
        Watching(currently_watching=currently_watching, currently_episode=currently_episode).save()
        pass
    except Exception as exception:
      raise exception

p = Populate()
p.execute_populate(50)