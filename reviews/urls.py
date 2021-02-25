from django.urls import path

from reviews.views import get_review

urlpatterns = [
    path('<review_id>', get_review)
]
