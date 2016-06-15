# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('solicitudes', '0004_auto_20160615_1550'),
    ]

    operations = [
        migrations.CreateModel(
            name='SolicitudVacaciones',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('inicio', models.DateField(default=datetime.datetime.today)),
                ('termino', models.DateField(default=datetime.datetime.today)),
            ],
        ),
    ]
