import os, django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from faker import Faker
import random
from tvshow.models import User, Tvshow

class Populate:
  Faker.seed(10)

  def __init__(self, fake=Faker('en_us')):
    self.fake = fake

  def populate_users(self, users):
    try:
      for _ in range(users):
        username = self.fake.name()
        email = '{}@{}'.format(username.lower(), self.fake.free_email_domain())
        email = email.replace(' ', '')
        password = '{}{}'.format(random.randrange(1000, 9999), 'xyzXYZ&')
        User(username=username, email=email, password=password).save()
    except Exception as exception:
      raise exception

  def populate_tvshows(self, tvshows):
    try:
      for _ in range(tvshows):
        title = '{}{}'.format('generic_title', _)
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
    except Exception as exception:
      raise exception

def execute_populate(p, range_):
  try:
    p.populate_users(range_)
    p.populate_tvshows(range_)
  except Exception as exception:
    print('Script could not pass request validation: ', exception)
    pass

p = Populate()
execute_populate(p, 50)