from django.db import models


class Item(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    image = models.ImageField()
    weight = models.PositiveSmallIntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
