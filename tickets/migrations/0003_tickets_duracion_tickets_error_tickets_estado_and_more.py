# Generated by Django 4.1.7 on 2023-03-15 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0002_tickets_fecha_solicitud'),
    ]

    operations = [
        migrations.AddField(
            model_name='tickets',
            name='duracion',
            field=models.CharField(choices=[('1', 'Una Sola Vez'), ('2', 'Todo el Mes'), ('3', 'Hasta FIN DE MES'), ('4', 'Hasta la fecha del Evento'), ('5', 'Una vez al Mes'), ('6', 'Dos veces al Mes'), ('7', 'Una semana'), ('8', 'Hasta teminar Material')], default=3, max_length=2),
        ),
        migrations.AddField(
            model_name='tickets',
            name='error',
            field=models.CharField(choices=[('1', 'No aprobado por Cliente'), ('2', 'Extemporaneo'), ('3', 'Uso de material indebido'), ('4', 'Error ortográfico o de dedo'), ('5', 'Información erronea')], default=3, max_length=2),
        ),
        migrations.AddField(
            model_name='tickets',
            name='estado',
            field=models.CharField(choices=[('1', 'Canceló la reunión'), ('2', 'Correciones'), ('3', 'Revisión por Diseño'), ('4', 'en Autorización Cliente'), ('5', 'Terminado'), ('6', 'Proceso'), ('7', 'Pausa por Cliente'), ('8', 'Registrado'), ('9', 'Asignado'), ('10', 'Cancelado por GS'), ('11', 'En espera de información'), ('12', 'Cancelado por pago'), ('13', 'Propuesta'), ('14', 'Canceló Cliente'), ('15', 'Pausa por GS')], default=3, max_length=2),
        ),
        migrations.AddField(
            model_name='tickets',
            name='frecuencia',
            field=models.CharField(choices=[('1', 'Una Sola Vez'), ('2', '1 vez a la semana'), ('3', '2 vez a la semana'), ('4', '3 vez a la semana'), ('5', 'Diario'), ('6', 'Lunes a Viernes'), ('7', 'Una vez al Mes'), ('8', 'Lunes a Sábado')], default=3, max_length=2),
        ),
        migrations.AddField(
            model_name='tickets',
            name='medio_origen',
            field=models.CharField(choices=[('1', 'WhatsApp - Mensaje'), ('2', 'WhatsApp - Audio'), ('3', 'Correo'), ('4', 'Llamada'), ('5', 'WEB- Ticket'), ('6', 'Reunión Cliente'), ('7', 'Evento'), ('8', 'Petición Interna'), ('9', 'Sesión Fotográfica'), ('10', 'Parrilla Mensual'), ('11', 'Video')], default=3, max_length=2),
        ),
        migrations.AddField(
            model_name='tickets',
            name='tipo_error',
            field=models.CharField(choices=[('1', 'Ortográfico'), ('2', 'Diseño'), ('3', 'Material Equivocado'), ('4', 'Sticker/Ticket en Whats'), ('5', 'Etiquetas Barrido'), ('6', 'Priorización'), ('7', 'Registro de Actividades')], default=3, max_length=2),
        ),
        migrations.AddField(
            model_name='tickets',
            name='uso',
            field=models.CharField(choices=[('1', 'Actualización de Datos'), ('2', 'Análisis'), ('3', 'Activación '), ('4', 'Impresión'), ('5', 'Galería RRSS '), ('6', 'Campaña RRSS '), ('7', 'Publicación RRSS'), ('8', 'WhatsApp'), ('9', 'Evento'), ('10', 'Historia Destacada'), ('11', 'Ebook'), ('12', 'Web'), ('13', 'Envío de Archivos'), ('14', 'Transmisión en Vivo'), ('15', 'Catálogo'), ('16', 'Video'), ('17', 'Planeación'), ('18', 'Carrusel Campaña'), ('19', 'Bocetaje'), ('20', 'Colaboradores'), ('21', 'Barrido Notificaciones'), ('22', 'ADM-Gestión'), ('23', 'Programación Actividades'), ('24', 'Revisión de Material'), ('25', 'Contacto Cliente'), ('26', 'Oficina'), ('27', 'Seguimiento Cuentas'), ('28', 'Metodología Interna'), ('29', 'Perifoneo'), ('30', 'Programar Historias'), ('31', 'Programar Publicación'), ('32', 'Publicar Galería (Album)'), ('33', 'Pantallas Publicitarias'), ('34', 'Presentación PPT'), ('35', 'Correo'), ('36', 'Catálogo Ebook'), ('37', 'Voz en off'), ('38', 'Diseño-Actualizaciones'), ('39', 'Diseño-Correcciones '), ('40', 'Propuesta'), ('41', 'Capacitación'), ('42', 'PDF'), ('43', 'Descarga de Material'), ('44', 'Networking'), ('45', 'Cobranza'), ('46', 'Capacitación al Personal'), ('47', 'Contabilidad'), ('48', 'Publicación Historias'), ('49', 'Logotipo')], default=3, max_length=2),
        ),
        migrations.AlterField(
            model_name='tickets',
            name='prioridad',
            field=models.CharField(choices=[('1', '1-URGENTE'), ('2', '2-Importante'), ('3', '3-Normal'), ('4', '4-Programado')], default=3, max_length=2),
        ),
    ]
