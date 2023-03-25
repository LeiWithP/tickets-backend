from rest_framework import routers
from django.urls import include, path
from knox import views as knox_views
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
    path('api/user/', views.get_user_data),
    path('api/exist/', views.user_exists),
    path('api/logout/', knox_views.LogoutView.as_view()),
    path('api/logoutall/', knox_views.LogoutAllView.as_view()),
]
