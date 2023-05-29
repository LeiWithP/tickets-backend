from rest_framework import routers
from django.urls import include, path
from knox import views as knox_views
from tickets import api, views

router = routers.DefaultRouter()

router.register('api/users', api.UserViewSet)
router.register('api/groups', api.GroupViewSet)
router.register('api/tickets', api.TicketsViewSet, 'tickets')
router.register('api/empresas', api.EmpresasViewSet, 'empresas')
router.register('api/parrillas', api.ParrillasViewSet, 'parrillas')
router.register('api/pentradas', api.ParrilasEntriesViewSet, 'pentradas')

urlpatterns = [
    path('', include(router.urls)),
    path('api/prioridades/', views.PrioridadListView.as_view()),
    path('api/estados/', views.EstadoListView.as_view()),
    path('api/actividades/', views.ActividadListView.as_view()),
    path('api/usos/', views.UsoListView.as_view()),
    path('api/frecuencias/', views.FrecuenciaListView.as_view()),
    path('api/duraciones/', views.DuracionListView.as_view()),
    path('api/dias/', views.DiaListView.as_view()),
    path('api/medios-origen/', views.MedioOrigenListView.as_view()),
    path('api/errores/', views.ErrorListView.as_view()),
    path('api/tipos-error/', views.TipoErrorListView.as_view()),
    path('api/user/', views.get_user_data),
    path('api/allusers/', views.get_all_users),
    path('api/exist/', views.user_exists),
    path('api/register/', views.register_api),
    path('api/login/', views.login_api),
    path('api/logout/', knox_views.LogoutView.as_view()),
    path('api/logoutall/', knox_views.LogoutAllView.as_view()),
    path('api/alltickets/', views.get_all_tickets),
]
