from rest_framework import routers
from .api import TicketsViewSet, EmpresasViewSet

router = routers.DefaultRouter()

router.register('api/tickets', TicketsViewSet, 'tickets')
router.register('api/empresas', EmpresasViewSet, 'empresas')

urlpatterns = router.urls
