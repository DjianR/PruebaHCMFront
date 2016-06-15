from django import forms
from .models import SolicitudVacante, SolicitudVacaciones

class SolFormV(forms.ModelForm):
    class Meta:
        model = SolicitudVacante
        exclude = ('aprobacion','encargado', 'fecha_creacion')

class SolFormVtion(forms.ModelForm):
    class Meta:
        model = SolicitudVacaciones
        exclude = ('aprobacion','encargado')

class SolFormV_aprobar(forms.ModelForm):
    class Meta:
        model = SolicitudVacante
        fields = ('aprobacion',"empleado")

class SolFormVtion_aprobar(forms.ModelForm):
    class Meta:
        model = SolicitudVacaciones
        fields = ('aprobacion',)
