# Generated by Django 4.2.2 on 2023-07-01 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_data_collected_browser'),
    ]

    operations = [
        migrations.AddField(
            model_name='data_collected',
            name='Os',
            field=models.CharField(blank=True, default=0, max_length=200, null=True),
        ),
    ]