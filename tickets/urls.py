from rest_framework import routers
from django.urls import include, path
from tickets import api, views
#from .api import UserViewSet, GroupViewSet
#from .api import TicketsViewSet, EmpresasViewSet

router = routers.DefaultRouter()

router.register('api/users', api.UserViewSet)
router.register('api/groups', api.GroupViewSet)
router.register('api/tickets', api.TicketsViewSet, 'tickets')
router.register('api/empresas', api.EmpresasViewSet, 'empresas')

urlpatterns = [
    path('', include(router.urls)),
    path('api/register/', views.register_api),
    path('api/login/', views.login_api),
]
