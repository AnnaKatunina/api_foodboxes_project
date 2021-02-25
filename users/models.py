from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    middle_name = models.CharField(max_length=64)
    phone = models.CharField(max_length=24)
    address = models.CharField(max_length=128)
