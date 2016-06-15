# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('solicitudes', '0002_remove_solicitudvacante_encargado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='solicitudvacante',
            name='aprobacion',
        ),
    ]
