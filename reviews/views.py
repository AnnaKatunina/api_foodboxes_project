from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from reviews.models import Review


@api_view(http_method_names=['GET'])
def get_review(request, pk):
    review = get_object_or_404(Review, pk=pk)
    return Response({
        'id': review.id,
        'author': review.author.id,
        'text': review.text,
        'created_at': review.created_at,
        'published_at': review.published_at,
        'status': review.status,
    })
