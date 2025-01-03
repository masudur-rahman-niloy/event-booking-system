# Generated by Django 5.1.3 on 2024-11-28 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventapp', '0008_alter_booking_booking_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='is_paid',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='booking',
            name='is_refunded',
            field=models.BooleanField(default=False),
        ),
    ]
