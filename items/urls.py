from django.urls import path

from items.views import get_item

urlpatterns = [
    path('<pk>', get_item)
]
