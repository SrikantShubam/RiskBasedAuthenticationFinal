# Generated by Django 4.2.2 on 2023-07-03 06:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_rename_system_time_data_collected_time_collected'),
    ]

    operations = [
        migrations.RenameField(
            model_name='data_collected',
            old_name='time_collected',
            new_name='system_time',
        ),
    ]