# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_car_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car_data',
            name='id',
        ),
        migrations.AddField(
            model_name='car_data',
            name='DTC',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='car_data',
            name='UUID',
            field=models.CharField(default=True, max_length=20, serialize=False, primary_key=True),
        ),
        migrations.AddField(
            model_name='car_data',
            name='average_fuel',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=2),
        ),
        migrations.AddField(
            model_name='car_data',
            name='battery_v',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=2),
        ),
        migrations.AddField(
            model_name='car_data',
            name='coolant_Temp',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='car_data',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 23, 5, 51, 56, 930551, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='car_data',
            name='duration',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='car_data',
            name='engine_load',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=2),
        ),
        migrations.AddField(
            model_name='car_data',
            name='fuel_consump_thistime',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='car_data',
            name='fuel_left',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=2),
        ),
        migrations.AddField(
            model_name='car_data',
            name='hard_accel',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='car_data',
            name='hard_breaks',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='car_data',
            name='hotcar_du',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='car_data',
            name='idle_duration',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=2),
        ),
        migrations.AddField(
            model_name='car_data',
            name='idle_fuel_consump',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=2),
        ),
        migrations.AddField(
            model_name='car_data',
            name='instant_fuel',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=2),
        ),
        migrations.AddField(
            model_name='car_data',
            name='max_rpm',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='car_data',
            name='max_speed',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='car_data',
            name='mileage',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='car_data',
            name='rpm',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='car_data',
            name='throttle_position',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=2),
        ),
    ]
