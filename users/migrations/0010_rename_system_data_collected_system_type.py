# Generated by Django 4.2.2 on 2023-07-03 06:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_data_collected_system'),
    ]

    operations = [
        migrations.RenameField(
            model_name='data_collected',
            old_name='system',
            new_name='system_type',
        ),
    ]