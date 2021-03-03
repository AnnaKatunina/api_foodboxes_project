from django.urls import path

from reviews.views import get_review

urlpatterns = [
    path('<pk>', get_review)
]
