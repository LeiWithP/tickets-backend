# Generated by Django 4.0 on 2023-05-27 15:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('tickets', '0028_parrillas_parrillasentry_delete_parrilas'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ParrillasEntry',
            new_name='ParrillasEntries',
        ),
    ]
