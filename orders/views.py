from django.shortcuts import get_object_or_404, render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from cart.models import Cart
from shop.models import Item
from .models import Order
from .models import OrderItem
from .serializers import OrderSerializer, OrderPostSerializer, OrderItemSerializer


class OrderAPI(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        cart = Cart(request)
        serializer = OrderPostSerializer()
        order = serializer.create(validated_data=request.data['order'])
        if cart:
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=get_object_or_404(Item, id=item['id']),
                                         price=item['price'],
                                         quantity=item['quantity'])
            cart.clear()
            return Response(status=200)
        return Response(status=203)

    def get(self, request):
        serializer = OrderSerializer(
            Order.objects.filter(user=request.user), many=True
        )
        return Response(serializer.data)


class OrderItemViewSet(ModelViewSet):
    serializer_class = OrderItemSerializer
    queryset = OrderItem.objects.all()
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['order']


def make_order_view(request):
    return render(request, 'orders/create.html')
