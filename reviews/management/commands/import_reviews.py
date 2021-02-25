import requests
from django.core.management import BaseCommand
from django.utils import timezone

from reviews.models import Review
from users.models import User

URL = 'https://raw.githubusercontent.com/stepik-a-w/drf-project-boxes/master/reviews.json'


class Command(BaseCommand):

    def handle(self, *args, **options):
        response = requests.get(url=URL).json()
        for review in response:
            if review['published_at'] == '':
                published_at = timezone.now
            else:
                published_at = review['published_at']
            if review['status'] == 'published':
                status = '2'
            elif review['status'] == 'hidden':
                status = '3'
            else:
                status = '1'
            Review.objects.get_or_create(
                id=review['id'],
                defaults={
                    'author': User.objects.get(id=review['author']),
                    'text': review['content'],
                    'created_at': review['created_at'],
                    'published_at': published_at,
                    'status': status,
                }
            )
        return
