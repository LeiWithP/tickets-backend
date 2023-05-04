from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.auth import AuthToken
from .serializers import RegisterSerializer
from django.contrib.auth.models import User
from .models import Tickets
from .catalogos import PRIORIDAD, ESTADO, ACTIVIDAD, USO, FRECUENCIA, DURACION, DIA, MEDIO_ORIGEN, ERROR, TIPO_ERROR
from .catalogos import prioridad_dict, estado_dict, actividad_dict, uso_dict, frecuencia_dict, duracion_dict, dia_dict, medio_origen_dict, error_dict, tipo_error_dict

class PrioridadListView(APIView):
    def get(self, request):
        return Response(prioridad_dict)
    
class EstadoListView(APIView):
    def get(self, request):
        return Response(estado_dict)
    
class ActividadListView(APIView):
    def get(self, request):
        return Response(actividad_dict)

class UsoListView(APIView):
    def get(self, request):
        return Response(uso_dict)

class FrecuenciaListView(APIView):
    def get(self, request):
        return Response(frecuencia_dict)

class DuracionListView(APIView):
    def get(self, request):
        return Response(duracion_dict)

class DiaListView(APIView):
    def get(self, request):
        return Response(dia_dict)

class MedioOrigenListView(APIView):
    def get(self, request):
        return Response(medio_origen_dict)

class ErrorListView(APIView):
    def get(self, request):
        return Response(error_dict)

class TipoErrorListView(APIView):
    def get(self, request):
        return Response(tipo_error_dict)

@api_view(['POST'])
def register_api(request):
    serializer = RegisterSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    user = serializer.save()
    _, token = AuthToken.objects.create(user)

    return Response()

@api_view(['POST'])
def login_api(request):
    serializer = AuthTokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data['user']
    _, token = AuthToken.objects.create(user)

    return Response({
        'user_info': {
            'id': user.id,
            'username': user.username,
            'email': user.email
            },
        'token': token
    })

@api_view(['GET'])
def get_user_data(request):
    user = request.user

    if user.is_authenticated:
        return Response({
            'id': user.id,
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'rol': user.groups.all()[0].name,
            'last_login': user.last_login
        })
    
    return Response({'error': 'No Autenticado'}, status=400)

@api_view(['GET'])
def get_all_users(request):
    users = User.objects.all()
    user_data = []
    
    for user in users:
        user_data.append({
            'id': str(user.id),
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'rol': user.groups.all()[0].name,
            'active': user.is_active,
            'last_login': user.last_login
        })
    return Response(user_data)

@api_view(['GET'])
def user_exists(request):
    user = request.user

    if user.is_authenticated:
        return Response({'exist': 'True'})
    
    return Response({'error': 'No Autenticado'}, status=400)

@api_view(['GET'])
def get_all_tickets(request):
    tickets = Tickets.objects.all()
    ticket_data = []
    
    for ticket in tickets:
        prioridad_str = dict(PRIORIDAD).get(ticket.prioridad, 'No especificado')
        estado_str = dict(ESTADO).get(ticket.estado, 'No especificado')
        actividad_str = dict(ACTIVIDAD).get(ticket.actividad, 'No especificado')
        uso_str = dict(USO).get(ticket.uso, 'No especificado')
        frecuencia_str = dict(FRECUENCIA).get(ticket.frecuencia, 'No especificado')
        duracion_str = dict(DURACION).get(ticket.duracion, 'No especificado')
        medio_origen_str = dict(MEDIO_ORIGEN).get(ticket.medio_origen, 'No especificado')
        error_str = dict(ERROR).get(ticket.error, 'No especificado')
        tipo_error_str = dict(TIPO_ERROR).get(ticket.tipo_error, 'No especificado')

        ticket_data.append({
            'id': str(ticket.id),
            'peticion': ticket.peticion,
            'medio_origen': medio_origen_str,
            'fecha_limite': ticket.fecha_limite,
            'prioridad': prioridad_str,
            'fecha_solicitud': ticket.fecha_solicitud,
            'servidor_ubicacion': ticket.servidor_ubicacion,
            'actividad': actividad_str,
            'uso': uso_str,
            'frecuencia': frecuencia_str,
            'duracion': duracion_str,
            'estado': estado_str,
            'fecha_entrega': ticket.fecha_entrega,
            'info_cliente': ticket.info_cliente,
            'observaciones': ticket.observaciones,
            'correcciones': ticket.correcciones,
            'error': error_str,
            'tipo_error': tipo_error_str,
            #'empresa': ticket.empresa,
            #'levanta_ticket': ticket.levanta_ticket,
            #'cliente_solicita': ticket.cliente_solicita,
            #'encargado': ticket.encargado,
            #'apoyo': ticket.apoyo,
        })
    return Response(ticket_data)