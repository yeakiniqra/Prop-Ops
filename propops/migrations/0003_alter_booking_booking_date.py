# Generated by Django 5.0.4 on 2024-04-26 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('propops', '0002_booking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='booking_date',
            field=models.DateTimeField(),
        ),
    ]
