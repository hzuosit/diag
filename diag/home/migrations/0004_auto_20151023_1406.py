# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20151023_0151'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car_data',
            name='date_time',
        ),
        migrations.AddField(
            model_name='car_data',
            name='data_end',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='car_data',
            name='date_start',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='car_data',
            name='time_end',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='car_data',
            name='time_start',
            field=models.IntegerField(null=True),
        ),
    ]
