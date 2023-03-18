from rest_framework import serializers
from .models import Tickets, Empresas

class EmpresasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresas
        fields = ('id', 'empresa', 'sucursal', 'direccion', 'telefono', 'correo',)

class TicketsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tickets
        fields = ('id', 'informacion', 'fecha_solicitud', 'prioridad', 'estado', 'uso', 'frecuencia', 'duracion', 'medio_origen', 'error', 'tipo_error',)
        read_only_fields = ('fecha_solicitud',)