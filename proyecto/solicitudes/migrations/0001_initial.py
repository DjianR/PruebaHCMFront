# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ResponsableRRHH',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='SolicitudVacante',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cargo', models.CharField(max_length=50)),
                ('vacantes', models.IntegerField(default=5)),
                ('tipo_cargo', models.CharField(max_length=2, choices=[('N', 'Nuevo'), ('R', 'Reemplazo')])),
                ('tipo_jornada', models.CharField(default=b'C', max_length=2, choices=[('C', 'Completa'), ('P', 'Part-Time')])),
                ('sueldo', models.IntegerField(null=True, blank=True)),
                ('comentarios', models.CharField(max_length=100, blank=True)),
                ('aprobacion', models.BooleanField(default=False)),
                ('empleado', models.ForeignKey(to='solicitudes.Empleado')),
                ('encargado', models.ForeignKey(to='solicitudes.ResponsableRRHH')),
            ],
        ),
    ]
