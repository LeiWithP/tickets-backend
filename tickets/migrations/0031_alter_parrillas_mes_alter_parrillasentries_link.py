# Generated by Django 4.0 on 2023-05-27 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0030_remove_parrillas_tipo_error'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parrillas',
            name='mes',
            field=models.CharField(blank=True, choices=[('1', 'ENERO'), ('2', 'FEBRERO'), ('3', 'MARZO'), ('4', 'ABRIL'), ('5', 'MAYO'), ('6', 'JUNIO'), ('7', 'JULIO'), ('8', 'AGOSTO'), ('9', 'SEPTIEMBRE'), ('10', 'OCTUBRE'), ('11', 'NOVIMEBRE'), ('12', 'DICIEMBRE')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='parrillasentries',
            name='link',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]