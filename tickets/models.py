from django.db import models
from datetime import datetime

PRIORIDAD = [
    ('1', '1-URGENTE'),
    ('2', '2-Importante'),
    ('3', '3-Normal'),
    ('4', '4-Programado'),
]

class Tickets(models.Model):
    informacion = models.CharField(max_length=250)
    fecha_solicitud = models.DateField(
        default=datetime.today
    )
    prioridad = models.CharField(
        max_length=1,
        choices=PRIORIDAD,
        default=3,
    )