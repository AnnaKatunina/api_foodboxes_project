import requests

from django.core.management import BaseCommand

from items.models import Item

URL = 'https://raw.githubusercontent.com/stepik-a-w/drf-project-boxes/master/foodboxes.json'


class Command(BaseCommand):

    def handle(self, *args, **options):
        response = requests.get(url=URL).json()

        for item_dict in response:
            Item.objects.get_or_create(
                id=item_dict['id'],
                defaults={
                    'title': item_dict['title'],
                    'description': item_dict['description'],
                    'image': f'items/foodb{item_dict["id"]}.jpg',
                    'weight': item_dict['weight_grams'],
                    'price': item_dict['price'],
                }
            )
        return
