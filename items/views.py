from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.viewsets import ReadOnlyModelViewSet

from items.filters import ItemFilter
from items.models import Item
from items.serializers import ItemSerializer


class ItemViewSet(ReadOnlyModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = ItemFilter
