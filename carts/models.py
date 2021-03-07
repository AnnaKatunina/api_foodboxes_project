from django.db import models

from items.models import Item
from users.models import User


class Cart(models.Model):
    items = models.ManyToManyField(Item, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class CartItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
