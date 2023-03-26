from django.contrib.auth.models import User, Group
from django.db.models import Q
from django.db import models
from datetime import datetime
from tickets import catalogos

class Empresas(models.Model):
    empresa = models.CharField(max_length=100)
    sucursal = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=10)
    correo = models.EmailField()

class Tickets(models.Model):
    empresa = models.ForeignKey(
        Empresas,
        on_delete=models.CASCADE,
        null=True,
    )
    peticion = models.CharField(max_length=250)
    medio_origen = models.CharField(
        max_length=2,
        choices=catalogos.MEDIO_ORIGEN,
        default=4,
    )
    levanta_ticket = models.ForeignKey(
        User,
        related_name="levanta", 
        on_delete=models.CASCADE,
        limit_choices_to=Q(groups__name = 'director general') 
            | Q(groups__name = 'director operativo')
            | Q(groups__name = 'creativo'),
        null=True,
    )
    cliente_solicita = models.ForeignKey(
        User,
        related_name="solicita",
        on_delete=models.CASCADE,
        limit_choices_to=Q(groups__name = 'cliente'),
        null=True,
    )
    fecha_limite = models.DateField(null=True,)
    prioridad = models.CharField(
        max_length=2,
        choices=catalogos.PRIORIDAD,
        default=3,
    )
    fecha_solicitud = models.DateTimeField(
        default=datetime.today,
    )
    servidor_ubicacion = models.CharField(max_length=500, blank=True)
    actividad = models.CharField(
        max_length=2,
        choices=catalogos.ACTIVIDAD,
        default=35,
    )
    uso = models.CharField(
        max_length=2,
        choices=catalogos.USO,
        default=2,
    )
    encargado = models.ForeignKey(
        User,
        related_name="encargado", 
        on_delete=models.CASCADE,
        limit_choices_to=Q(groups__name = 'director operativo')
            | Q(groups__name = 'creativo'),
        null=True,
    )
    apoyo = models.ForeignKey(
        User,
        related_name="apoyo", 
        on_delete=models.CASCADE,
        limit_choices_to=Q(groups__name = 'creativo'),
        null=True,
    )
    #redes sociales...
    frecuencia = models.CharField(
        max_length=2,
        choices=catalogos.FRECUENCIA,
        blank=True,
        null=True,
    )
    #dias habilitados
    duracion = models.CharField(
        max_length=2,
        choices=catalogos.DURACION,
        blank=True,
        null=True,
    )
    estado = models.CharField(
        max_length=2,
        choices=catalogos.ESTADO,
        default=11,
    )
    fecha_entrega = models.DateTimeField(null=True,)
    info_cliente = models.CharField(max_length=500, blank=True,)
    observaciones = models.CharField(max_length=500, blank=True,)
    correcciones = models.CharField(max_length=500, blank=True,)
    error = models.CharField(
        max_length=2,
        choices=catalogos.ERROR,
        blank=True,
        null=True,
    )
    tipo_error = models.CharField(
        max_length=2,
        choices=catalogos.TIPO_ERROR,
        blank=True,
        null=True,
    )