from django.urls import path

from items.views import get_item

urlpatterns = [
    path('<item_id>', get_item)
]
