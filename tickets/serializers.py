from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Tickets, Empresas

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class EmpresasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresas
        fields = ('id', 'empresa', 'sucursal', 'direccion', 'telefono', 'correo',)

class TicketsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tickets
        fields = ('id', 'informacion', 'fecha_solicitud', 'prioridad', 'estado', 'uso', 'frecuencia', 'duracion', 'medio_origen', 'error', 'tipo_error',)
        read_only_fields = ('fecha_solicitud',)