# Generated by Django 4.2.2 on 2023-07-01 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_data_collected_browser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data_collected',
            name='browser',
            field=models.CharField(blank=True, default=0, max_length=20, null=True),
        ),
    ]
