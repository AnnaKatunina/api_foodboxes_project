from django.urls import path
from rest_framework.authtoken import views

from users.views import RegisterView, CurrentUserView

urlpatterns = [
    path('auth/login/', views.obtain_auth_token),
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('current/', CurrentUserView.as_view(), name='current'),
]
