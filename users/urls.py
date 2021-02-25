from django.urls import path

from users.views import get_user

urlpatterns = [
    path('<user_id>', get_user)
]
