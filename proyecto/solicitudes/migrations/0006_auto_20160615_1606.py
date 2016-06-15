# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('solicitudes', '0005_solicitudvacaciones'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitudvacaciones',
            name='termino',
            field=models.DateField(default=datetime.datetime(2016, 6, 22, 16, 6, 35, 570401)),
        ),
    ]
