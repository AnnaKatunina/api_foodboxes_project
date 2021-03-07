from django.urls import path
from rest_framework.routers import DefaultRouter

from carts.views import CartItemViewSet, CartViewSet


cart_detail = CartViewSet.as_view({
    'get': 'retrieve',
})

urlpatterns = [
    path('', cart_detail, name='carts'),
]

router = DefaultRouter()
router.register('items', CartItemViewSet, basename='cart_item')
urlpatterns += router.urls
