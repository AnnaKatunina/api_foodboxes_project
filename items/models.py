from django.core.files.storage import FileSystemStorage
from django.db import models

from foodboxes_project import settings

fs = FileSystemStorage(location=settings.STATIC_ROOT)


class Item(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    image = models.ImageField(upload_to="items", storage=fs)
    weight = models.PositiveSmallIntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
