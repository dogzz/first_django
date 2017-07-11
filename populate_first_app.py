import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first.settings')

import django
django.setup()


import random
from first_app.models import AccessRecord, Webpage, Topic, User
from faker import Faker

fakegen = Faker()
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']


def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t


def populate(N=5):
    for entry in range(N):
        top = add_topic()
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        webpg = Webpage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]

        acc_rec = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)[0]


def populate_user(N=5):
    for entry in range(N):
        user = User.objects.get_or_create(first_name=fakegen.first_name(), last_name=fakegen.last_name(),
                                          email=fakegen.safe_email())

if __name__ == '__main__':
    populate_user(20)
    print('Done')