from rest_framework import viewsets

from ..models import Position, Manager
from .serializers import PositionSerializer, ManagerSerializer


class PositionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer
    lookup_field = 'slug'


class ManagerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer
