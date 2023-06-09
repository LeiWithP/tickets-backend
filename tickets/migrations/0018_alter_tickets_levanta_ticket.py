# Generated by Django 4.0 on 2023-03-19 20:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('tickets', '0017_alter_tickets_cliente_solicita'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tickets',
            name='levanta_ticket',
            field=models.ForeignKey(limit_choices_to={'groups__name': 'creativo'}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='levanta', to='auth.user'),
        ),
    ]
