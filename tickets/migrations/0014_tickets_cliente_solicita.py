# Generated by Django 4.0 on 2023-03-19 19:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('tickets', '0013_tickets_levanta_ticket_clientes'),
    ]

    operations = [
        migrations.AddField(
            model_name='tickets',
            name='cliente_solicita',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='solicita', to='auth.user'),
        ),
    ]
