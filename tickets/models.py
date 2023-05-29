from django.contrib.auth.models import User, Group
from django.db.models import Q
from django.db import models
from datetime import datetime
from tickets import catalogos

class Empresas(models.Model):
    empresa = models.CharField(max_length=100)
    # sucursal = models.CharField(max_length=100)
    # direccion = models.CharField(max_length=100)
    # telefono = models.CharField(max_length=10)
    # correo = models.EmailField()
    def __str__(self) -> str:
        return self.empresa

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
        limit_choices_to=Q(groups__name = 'DG') 
            | Q(groups__name = 'DO')
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
        max_length=10,
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
        limit_choices_to=Q(groups__name = 'DG')
            | Q(groups__name = 'DO')
            | Q(groups__name = 'creativo'),
        null=True,
    )
    apoyo = models.ForeignKey(
        User,
        related_name="apoyo", 
        on_delete=models.CASCADE,
        limit_choices_to=Q(groups__name = 'DO')
            | Q(groups__name = 'DO')
            | Q(groups__name = 'creativo'),
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

    def __str__(self) -> str:
        return self.peticion

class Parrillas(models.Model):
    parrilla = models.CharField(max_length=100)
    empresa = models.ForeignKey(
        Empresas,
        on_delete=models.CASCADE,
        null=True,
    )
    mes = models.CharField(
        max_length=2,
        choices=catalogos.MES,
        blank=True,
        null=True,
    )

    def __str__(self) -> str:
        return self.parrilla

class ParrillasEntries(models.Model):
    parrilla = models.ForeignKey(
        Parrillas,
        on_delete=models.CASCADE,
    )
    fecha = models.DateTimeField(
        default=datetime.today,
    )
    objetivo = models.CharField(
        max_length=2,
        choices=catalogos.OBJETIVO,
        blank=True,
        null=True,
    )
    tema = models.CharField(max_length=200, blank=True,)
    copy = models.CharField(max_length=1000, blank=True,)
    frase = models.CharField(max_length=500, blank=True,)
    
    link = models.CharField(max_length=500, blank=True,)
    tipos_contenido = models.CharField(
        max_length=2,
        choices=catalogos.TIPO_CONTENIDO,
        blank=True,
        null=True,
    )
    plataforma = models.CharField(
        max_length=2,
        choices=catalogos.PLATAFORMA,
        blank=True,
        null=True,
    )
    elaborado = models.ForeignKey(
        User,
        related_name="elaborado", 
        on_delete=models.CASCADE,
        limit_choices_to=Q(groups__name = 'DO')
            | Q(groups__name = 'creativo')
            | Q(groups__name = 'cliente'),
        null=True,
    )
    ticket = models.ForeignKey(
        Tickets,
        on_delete=models.CASCADE,
        null=True,
    )