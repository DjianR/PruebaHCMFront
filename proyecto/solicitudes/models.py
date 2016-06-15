from django.db import models
from datetime import date, timedelta
import sys, datetime, time

# Create your models here.
class Empleado(models.Model):
    nombre = models.CharField(blank=True, max_length=50)

    def __unicode__(self):
        return u"%s" % self.nombre

class ResponsableRRHH(models.Model):
    nombre = models.CharField(blank=True, max_length=50)

    def __unicode__(self):
        return u"%s" % self.nombre


class SolicitudVacante(models.Model):
    TIPO_CARGO = (
        (u'N', u'Nuevo'),
        (u'R', u'Reemplazo'),
    )
    TIPO_JORNADA = (
        (u'C', u'Completa'),
        (u'P', u'Part-Time'),
    )
    empleado = models.ForeignKey(Empleado, null=True)
    vacantes = models.IntegerField(default=5)
    tipo_cargo = models.CharField(max_length=2, choices=TIPO_CARGO, null=True)
    tipo_jornada = models.CharField(default="C",max_length=2, choices=TIPO_JORNADA)
    sueldo = models.IntegerField(blank=True, null=True)
    comentarios = models.CharField(blank=True, max_length=100)
    fecha_creacion = models.DateField(default=datetime.datetime.today)

    aprobacion = models.BooleanField(default=False)
    encargado = models.ForeignKey(ResponsableRRHH, null=True)

    def __unicode__(self):
        return u"%s %s %s" % (self.empleado, self.vacantes, self.tipo_cargo)

class SolicitudVacaciones(models.Model):
    aprobacion = models.BooleanField(default=False)
    fecha_creacion = models.DateField(default=datetime.datetime.today)
    empleado = models.ForeignKey(Empleado, null=True)
    inicio = models.DateField(default=datetime.datetime.today)
    termino = models.DateField(default=datetime.datetime.today() + timedelta(days=7) )
    def __unicode__(self):
        return u"%s" % (self.empleado)
