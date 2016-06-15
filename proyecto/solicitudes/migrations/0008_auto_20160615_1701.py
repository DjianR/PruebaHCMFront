# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('solicitudes', '0007_auto_20160615_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitudvacaciones',
            name='termino',
            field=models.DateField(default=datetime.datetime(2016, 6, 22, 17, 1, 7, 506361)),
        ),
        migrations.AlterField(
            model_name='solicitudvacante',
            name='cargo',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='solicitudvacante',
            name='tipo_cargo',
            field=models.CharField(max_length=2, null=True, choices=[('N', 'Nuevo'), ('R', 'Reemplazo')]),
        ),
    ]
