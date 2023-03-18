from .models import Tickets, Empresas
from rest_framework import viewsets, permissions
from .serializers import TicketsSerializer, EmpresasSerializer

class EmpresasViewSet(viewsets.ModelViewSet):
    queryset = Empresas.objects.all()
    permissions_classes = [permissions.AllowAny]
    serializer_class = EmpresasSerializer

class TicketsViewSet(viewsets.ModelViewSet):
    queryset = Tickets.objects.all()
    permissions_classes = [permissions.AllowAny]
    serializer_class = TicketsSerializer