from rest_framework import routers
from django.urls import include, path
from knox import views as knox_views
from tickets import api, views

router = routers.DefaultRouter()

router.register('api/users', api.UserViewSet)
router.register('api/groups', api.GroupViewSet)
router.register('api/tickets', api.TicketsViewSet, 'tickets')
router.register('api/empresas', api.EmpresasViewSet, 'empresas')

urlpatterns = [
    path('', include(router.urls)),
    path('api/prioridad/', views.PrioridadListView.as_view()),
    path('api/estado/', views.EstadoListView.as_view()),
    path('api/actividad/', views.ActividadListView.as_view()),
    path('api/uso/', views.UsoListView.as_view()),
    path('api/frecuencia/', views.FrecuenciaListView.as_view()),
    path('api/duracion/', views.DuracionListView.as_view()),
    path('api/dia/', views.DiaListView.as_view()),
    path('api/medio-origen/', views.MedioOrigenListView.as_view()),
    path('api/error/', views.ErrorListView.as_view()),
    path('api/tipo-error/', views.TipoErrorListView.as_view()),
    path('api/register/', views.register_api),
    path('api/login/', views.login_api),
    path('api/user/', views.get_user_data),
    path('api/allusers/', views.get_all_users),
    path('api/exist/', views.user_exists),
    path('api/logout/', knox_views.LogoutView.as_view()),
    path('api/logoutall/', knox_views.LogoutAllView.as_view()),
]
