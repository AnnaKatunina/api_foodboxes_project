from rest_framework.serializers import ModelSerializer, ReadOnlyField
from rest_framework import serializers

from carts.models import Cart, CartItem


class CartItemSerializer(ModelSerializer):

    total_price = ReadOnlyField()
    price = serializers.DecimalField(source='item.price', max_digits=8, decimal_places=2)

    class Meta:
        model = CartItem
        fields = ['id', 'item', 'quantity', 'price', 'total_price']
        read_only_fields = ['id', 'price', 'total_price']


class CartSerializer(ModelSerializer):

    total_cost = ReadOnlyField()
    items = CartItemSerializer(many=True, required=False)

    class Meta:
        model = Cart
        fields = ['id', 'items', 'total_cost']
