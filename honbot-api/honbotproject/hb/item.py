from django.core.cache import cache

from .models import Item
from .serializers import ItemSerializer

from rest_framework import viewsets
from rest_framework.response import Response


class ItemsViewSet(viewsets.ViewSet):
    """
    Viewset for retreiving players
    """
    def list(self, request):
        data = cache.get('items')
        if not data:
            queryset = Item.objects.all()
            data = ItemSerializer(queryset, many=True).data
            cache.set('items', data, 3600)
        return Response(data)
