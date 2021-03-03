from django.urls import path

from users.views import get_user

urlpatterns = [
    path('<pk>', get_user)
]
