# Generated by Django 4.0 on 2023-03-18 21:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0006_alter_tickets_duracion_alter_tickets_error_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tickets',
            name='fecha_solicitud',
            field=models.DateTimeField(default=datetime.datetime.today),
        ),
    ]