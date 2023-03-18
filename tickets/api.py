from .models import Tickets, Empresas
from rest_framework import viewsets, permissions
from django.contrib.auth.models import User, Group
from .serializers import UserSerializer, GroupSerializer
from .serializers import TicketsSerializer, EmpresasSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class EmpresasViewSet(viewsets.ModelViewSet):
    queryset = Empresas.objects.all()
    permissions_classes = [permissions.AllowAny]
    serializer_class = EmpresasSerializer

class TicketsViewSet(viewsets.ModelViewSet):
    queryset = Tickets.objects.all()
    permissions_classes = [permissions.AllowAny]
    serializer_class = TicketsSerializer