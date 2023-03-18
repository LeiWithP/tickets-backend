# Generated by Django 4.0 on 2023-03-18 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0004_empresas'),
    ]

    operations = [
        migrations.AddField(
            model_name='tickets',
            name='actividad',
            field=models.CharField(choices=[('1', 'Web'), ('2', 'Evento'), ('3', '3D'), ('4', 'Edición Fotografía'), ('5', 'Diseño Gráfico'), ('6', 'Video'), ('7', 'Video - Grabación'), ('8', 'Fotografía'), ('9', 'Redes Sociales'), ('10', 'ADM-Gestión'), ('11', 'Auto-Capacitación'), ('12', 'Capacitación'), ('13', 'Video- Animación'), ('14', 'Copy'), ('15', 'Presentación'), ('16', 'Envio Material'), ('17', 'Mantenimiento'), ('18', 'Diseño Editorial'), ('19', 'Revisión de Cuentas'), ('20', 'Diseño-Correcciones '), ('21', 'Grabación Voz'), ('22', 'Contacto Cliente'), ('23', 'Hacer Café'), ('24', 'Edición-Correcciones '), ('25', 'Cobranza'), ('26', 'Pago Nómina'), ('27', 'Compra Insumos'), ('28', 'Acomodo Insumos'), ('29', 'Reunión con Cliente'), ('30', 'Limpieza'), ('31', 'Diseño-Actualizaciones'), ('32', 'Networking'), ('33', 'Actualización'), ('34', 'Re - Edición '), ('35', 'Ayuda'), ('36', 'Audio - Edición '), ('37', 'Cotización'), ('38', 'Configuración'), ('39', 'Gestoria Proveedores'), ('40', 'Foto y Video'), ('41', 'Soporte Digital'), ('42', 'Planeación'), ('43', 'Video- Edición'), ('44', 'Fotografía - Revelado '), ('45', 'Facturación'), ('46', 'Captura de Datos'), ('47', 'Diseño y Redes Sociales'), ('48', 'Publicación -Blog')], default=35, max_length=2),
        ),
        migrations.AlterField(
            model_name='tickets',
            name='duracion',
            field=models.CharField(choices=[('1', 'Una Sola Vez'), ('2', 'Todo el Mes'), ('3', 'Hasta FIN DE MES'), ('4', 'Hasta la fecha del Evento'), ('5', 'Una vez al Mes'), ('6', 'Dos veces al Mes'), ('7', 'Una semana'), ('8', 'Hasta teminar Material')], default=1, max_length=2),
        ),
        migrations.AlterField(
            model_name='tickets',
            name='estado',
            field=models.CharField(choices=[('1', 'Canceló la reunión'), ('2', 'Correciones'), ('3', 'Revisión por Diseño'), ('4', 'en Autorización Cliente'), ('5', 'Terminado'), ('6', 'Proceso'), ('7', 'Pausa por Cliente'), ('8', 'Registrado'), ('9', 'Asignado'), ('10', 'Cancelado por GS'), ('11', 'En espera de información'), ('12', 'Cancelado por pago'), ('13', 'Propuesta'), ('14', 'Canceló Cliente'), ('15', 'Pausa por GS')], default=11, max_length=2),
        ),
        migrations.AlterField(
            model_name='tickets',
            name='frecuencia',
            field=models.CharField(choices=[('1', 'Una Sola Vez'), ('2', '1 vez a la semana'), ('3', '2 vez a la semana'), ('4', '3 vez a la semana'), ('5', 'Diario'), ('6', 'Lunes a Viernes'), ('7', 'Una vez al Mes'), ('8', 'Lunes a Sábado')], default=1, max_length=2),
        ),
        migrations.AlterField(
            model_name='tickets',
            name='medio_origen',
            field=models.CharField(choices=[('1', 'WhatsApp - Mensaje'), ('2', 'WhatsApp - Audio'), ('3', 'Correo'), ('4', 'Llamada'), ('5', 'WEB- Ticket'), ('6', 'Reunión Cliente'), ('7', 'Evento'), ('8', 'Petición Interna'), ('9', 'Sesión Fotográfica'), ('10', 'Parrilla Mensual'), ('11', 'Video')], default=4, max_length=2),
        ),
        migrations.AlterField(
            model_name='tickets',
            name='uso',
            field=models.CharField(choices=[('1', 'Actualización de Datos'), ('2', 'Análisis'), ('3', 'Activación '), ('4', 'Impresión'), ('5', 'Galería RRSS '), ('6', 'Campaña RRSS '), ('7', 'Publicación RRSS'), ('8', 'WhatsApp'), ('9', 'Evento'), ('10', 'Historia Destacada'), ('11', 'Ebook'), ('12', 'Web'), ('13', 'Envío de Archivos'), ('14', 'Transmisión en Vivo'), ('15', 'Catálogo'), ('16', 'Video'), ('17', 'Planeación'), ('18', 'Carrusel Campaña'), ('19', 'Bocetaje'), ('20', 'Colaboradores'), ('21', 'Barrido Notificaciones'), ('22', 'ADM-Gestión'), ('23', 'Programación Actividades'), ('24', 'Revisión de Material'), ('25', 'Contacto Cliente'), ('26', 'Oficina'), ('27', 'Seguimiento Cuentas'), ('28', 'Metodología Interna'), ('29', 'Perifoneo'), ('30', 'Programar Historias'), ('31', 'Programar Publicación'), ('32', 'Publicar Galería (Album)'), ('33', 'Pantallas Publicitarias'), ('34', 'Presentación PPT'), ('35', 'Correo'), ('36', 'Catálogo Ebook'), ('37', 'Voz en off'), ('38', 'Diseño-Actualizaciones'), ('39', 'Diseño-Correcciones '), ('40', 'Propuesta'), ('41', 'Capacitación'), ('42', 'PDF'), ('43', 'Descarga de Material'), ('44', 'Networking'), ('45', 'Cobranza'), ('46', 'Capacitación al Personal'), ('47', 'Contabilidad'), ('48', 'Publicación Historias'), ('49', 'Logotipo')], default=2, max_length=2),
        ),
    ]
