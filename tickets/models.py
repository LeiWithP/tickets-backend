from django.db import models
from datetime import datetime
from tickets import catalogos

class Empresas(models.Model):
    empresa = models.CharField(max_length=100)
    sucursal = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    telefono = models.IntegerField(max_length=10)
    correo = models.EmailField()

class Tickets(models.Model):
    informacion = models.CharField(max_length=250)
    fecha_solicitud = models.DateField(
        default=datetime.today
    )
    prioridad = models.CharField(
        max_length=2,
        choices=catalogos.PRIORIDAD,
        default=3,
    )
    estado = models.CharField(
        max_length=2,
        choices=catalogos.ESTADO,
        default=3,
    )
    uso = models.CharField(
        max_length=2,
        choices=catalogos.USO,
        default=3,
    )
    frecuencia = models.CharField(
        max_length=2,
        choices=catalogos.FRECUENCIA,
        default=3,
    )
    duracion = models.CharField(
        max_length=2,
        choices=catalogos.DURACION,
        default=3,
    )
    medio_origen = models.CharField(
        max_length=2,
        choices=catalogos.MEDIO_ORIGEN,
        default=3,
    )
    error = models.CharField(
        max_length=2,
        choices=catalogos.ERROR,
        default=3,
    )
    tipo_error = models.CharField(
        max_length=2,
        choices=catalogos.TIPO_ERROR,
        default=3,
    )