from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ReadOnlyModelViewSet

from shop.serializers import ItemSerializer, UserItemRelationSerializer
from .models import Item, UserItemRelation


class ItemsViewSet(ReadOnlyModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filter_fields = ['id', 'price', 'available']
    search_fields = ['title', 'description']
    ordering_fields = ['price']

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class LikeAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserItemRelationSerializer(
            UserItemRelation.objects.filter(user=request.user, like=True),
            many=True
        )
        return Response(data=serializer.data)

    def post(self, request):
        relation, _ = UserItemRelation.objects\
            .get_or_create(user=request.user, item_id=request.data['itemId'])
        relation.like = request.data['like']
        relation.save()
        return Response('Liked', status=200)
