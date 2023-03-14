from .models import Tickets
from rest_framework import viewsets, permissions
from .serializers import TicketsSerializer

class TicketsViewSet(viewsets.ModelViewSet):
    queryset = Tickets.objects.all()
    permissions_classes = [permissions.AllowAny]
    serializer_class = TicketsSerializer