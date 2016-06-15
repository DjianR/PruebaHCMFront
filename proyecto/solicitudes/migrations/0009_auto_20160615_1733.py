# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('solicitudes', '0008_auto_20160615_1701'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='solicitudvacante',
            name='cargo',
        ),
        migrations.AlterField(
            model_name='solicitudvacaciones',
            name='termino',
            field=models.DateField(default=datetime.datetime(2016, 6, 22, 17, 33, 23, 214658)),
        ),
    ]
