from django.contrib.auth.models import User, Group
from rest_framework import serializers, validators
from .models import Tickets, Empresas

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        #fields = ['id', 'first_name', 'last_name', 'username']
        fields = ['id', 'username', 'email']

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name', ]
        extra_kwargs = {
            'password': {'write_only': True},
            'email': {
                'required': True,
                'allow_blank': False,
                'validators': [
                    validators.UniqueValidator(
                        User.objects.all(), 'ya existe una usuario con ese email'
                    )
                ]
            }
        }

    def create(self, validated_data):
        username = validated_data.get('username')
        password = validated_data.get('password')
        email = validated_data.get('email')
        first_name = validated_data.get('first_name')
        last_name = validated_data.get('last_name')

        user = User.objects.create(
            username = username,
            password = password,
            email = email,
            first_name = first_name,
            last_name = last_name
        )

        return user

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class EmpresasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresas
        fields = '__all__'
        #fields = ('id', 'empresa', 'sucursal', 'direccion', 'telefono', 'correo',)

class TicketsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tickets
        #fields = ('id', 'informacion', 'fecha_solicitud', 'prioridad', 'estado', 'actividad', 'uso', 'frecuencia', 'duracion', 'medio_origen', 'error', 'tipo_error',)
        fields = '__all__'
        read_only_fields = ('fecha_solicitud', 'fecha_entrega',)