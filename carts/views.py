from rest_framework import mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from carts.models import Cart, CartItem
from carts.paginators import CartItemLimitOffsetPagination
from carts.serializers import CartSerializer, CartItemSerializer


class CartViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def retrieve(self, request):
        cart = self.queryset.get_or_create(user=request.user)
        serializer = CartSerializer(cart[0])
        return Response(serializer.data)


class CartItemViewSet(ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    pagination_class = CartItemLimitOffsetPagination
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
