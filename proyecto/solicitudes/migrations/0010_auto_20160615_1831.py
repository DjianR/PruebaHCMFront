# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('solicitudes', '0009_auto_20160615_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitudvacaciones',
            name='termino',
            field=models.DateField(default=datetime.datetime(2016, 6, 22, 18, 31, 48, 540991)),
        ),
    ]
