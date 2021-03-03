import re
import requests
from django.core.management import BaseCommand

from users.models import User

URL = 'https://raw.githubusercontent.com/stepik-a-w/drf-project-boxes/master/recipients.json'


class Command(BaseCommand):

    def handle(self, *args, **options):
        response = requests.get(url=URL).json()

        for dict_user in response:
            user, created = User.objects.get_or_create(
                id=dict_user['id'],
                defaults={
                    'username': re.findall('(\S+)@', dict_user['email'])[0],
                    'first_name': dict_user['info']['name'],
                    'last_name': dict_user['info']['surname'],
                    'email': dict_user['email'],
                    'middle_name': dict_user['info']['patronymic'],
                    'phone': dict_user['contacts']['phoneNumber'],
                    'address': dict_user['city_kladr'],
                }
            )
            user.set_password(dict_user['password'])
            user.save()
        return
