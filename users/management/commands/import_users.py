import re
import requests
from django.core.management import BaseCommand

from users.models import User

URL = 'https://raw.githubusercontent.com/stepik-a-w/drf-project-boxes/master/recipients.json'


class Command(BaseCommand):

    def handle(self, *args, **options):
        response = requests.get(url=URL).json()

        for user in response:
            User.objects.get_or_create(
                username=re.findall('(\S+)@', user['email'])[0],
                defaults={
                    'id': user['id'],
                    'first_name': user['info']['name'],
                    'last_name': user['info']['surname'],
                    'email': user['email'],
                    'password': user['password'],
                    'middle_name': user['info']['patronymic'],
                    'phone': user['contacts']['phoneNumber'],
                    'address': user['city_kladr'],
                }
            )
        return
