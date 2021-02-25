from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from rest_framework.decorators import api_view

from rest_framework.response import Response

from items.models import Item


@api_view(http_method_names=['GET'])
def get_item(request, item_id):
    try:
        item = Item.objects.get(id=item_id)
        return Response({
            'id': item.id,
            'title': item.title,
            'description': item.description,
            'image': str(item.image),
            'weight': item.weight,
            'price': str(item.price),
        })
    except ObjectDoesNotExist:
        raise Http404()
