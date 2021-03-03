from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from users.models import User


@api_view(http_method_names=['GET'])
def get_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    return Response({
        'id': user.id,
        'username': user.username,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'middle_name': user.middle_name,
        'email': user.email,
        'phone': user.phone,
        'address': user.address,
    })
