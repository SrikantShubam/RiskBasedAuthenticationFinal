# Generated by Django 4.2.2 on 2023-07-03 08:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_rename_time_collected_data_collected_system_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='data_collected',
            name='start_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]