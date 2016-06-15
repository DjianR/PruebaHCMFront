# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('solicitudes', '0003_remove_solicitudvacante_aprobacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='solicitudvacante',
            name='aprobacion',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='solicitudvacante',
            name='encargado',
            field=models.ForeignKey(to='solicitudes.ResponsableRRHH', null=True),
        ),
        migrations.AlterField(
            model_name='solicitudvacante',
            name='empleado',
            field=models.ForeignKey(to='solicitudes.Empleado', null=True),
        ),
    ]
