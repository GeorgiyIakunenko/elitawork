from rest_framework import routers

from .views import PositionViewSet, ManagerViewSet

router = routers.DefaultRouter()
router.register(r'positions', PositionViewSet)
router.register(r'managers', ManagerViewSet)
