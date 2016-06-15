# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('solicitudes', '0006_auto_20160615_1606'),
    ]

    operations = [
        migrations.AddField(
            model_name='solicitudvacaciones',
            name='empleado',
            field=models.ForeignKey(to='solicitudes.Empleado', null=True),
        ),
        migrations.AlterField(
            model_name='solicitudvacaciones',
            name='termino',
            field=models.DateField(default=datetime.datetime(2016, 6, 22, 16, 7, 28, 158365)),
        ),
    ]
