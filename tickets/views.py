from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.auth import AuthToken
from .serializers import RegisterSerializer
from django.contrib.auth.models import User
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
