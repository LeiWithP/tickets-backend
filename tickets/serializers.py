from rest_framework import serializers
from .models import Tickets

class TicketsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tickets
        fields = ('id', 'informacion', 'fecha_solicitud', 'prioridad')
        read_only_fields = ('fecha_solicitud',)