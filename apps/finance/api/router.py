from .views import ProductViewSet, OrderViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(prefix='products',viewset=ProductViewSet)
router.register(prefix='orders',viewset=OrderViewSet)