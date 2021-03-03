from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from users.models import User


class Review(models.Model):

    class Status(models.TextChoices):
        published = 'опубликован', _('опубликован')
        hidden = 'отклонен', _('отклонен')
        new = 'на модерации', _('на модерации')

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    published_at = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=64, choices=Status.choices)
