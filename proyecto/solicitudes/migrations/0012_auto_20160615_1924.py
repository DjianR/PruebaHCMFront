# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('solicitudes', '0011_auto_20160615_1833'),
    ]

    operations = [
        migrations.AddField(
            model_name='solicitudvacaciones',
            name='fecha_creacion',
            field=models.DateField(default=datetime.datetime.today),
        ),
        migrations.AddField(
            model_name='solicitudvacante',
            name='fecha_creacion',
            field=models.DateField(default=datetime.datetime.today),
        ),
        migrations.AlterField(
            model_name='solicitudvacaciones',
            name='termino',
            field=models.DateField(default=datetime.datetime(2016, 6, 22, 19, 24, 8, 497127)),
        ),
    ]
