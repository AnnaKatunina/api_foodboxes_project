from django.db import models
from django.utils import timezone

from users.models import User


class Review(models.Model):

    STATUS_CHOICES = (
        ('1', 'на модерации'),
        ('2', 'опубликован'),
        ('3', 'отклонен'),
    )

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateField(default=timezone.now)
    published_at = models.DateField(default=timezone.now)
    status = models.CharField(max_length=64, choices=STATUS_CHOICES)
