from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from items.models import Item


@api_view(http_method_names=['GET'])
def get_item(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return Response({
        'id': item.id,
        'title': item.title,
        'description': item.description,
        'image': str(item.image),
        'weight': item.weight,
        'price': str(item.price),
    })
