from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import SolicitudVacante, SolicitudVacaciones
from .forms import SolFormV, SolFormVtion, SolFormV_aprobar, SolFormVtion_aprobar

# Create your views here.
def inicio(request):
	return render(request, 'solicitudes/inicio.html')

def empleado(request):
	return render(request, 'solicitudes/empleado.html')
def encargadoRRHH(request):
	return render(request, 'solicitudes/encargadoRRHH.html')


def nuevaVacante(request):
	nueva_sol = SolicitudVacante()

	if request.method == 'POST':
		formulario = SolFormV(request.POST, instance = nueva_sol)
		if formulario.is_valid():
			formulario.save()
			nueva_sol.save()
			return HttpResponseRedirect('/solicitudes/')
	else:
		formulario = SolFormV(request.POST, instance = nueva_sol)
	return render(request, 'solicitudes/new_solicitudVacante.html', {'formulario': formulario})

def nuevaVacacion(request):
	nueva_sol = SolicitudVacaciones()
	if request.method == 'POST':
		formulario = SolFormVtion(request.POST, instance = nueva_sol)
		if formulario.is_valid():
			formulario.save()
			nueva_sol.save()
			return HttpResponseRedirect('/solicitudes/')
	else:
		formulario = SolFormVtion(request.POST, instance = nueva_sol)
	return render(request, 'solicitudes/new_solicitudVacacion.html', {'formulario': formulario})

def verVacante(request):
	lista = SolicitudVacante.objects.all()

	context =  {'lista': lista}
	return render(request, 'solicitudes/ver_sol_vacante.html', context)

def verVacacion(request):
	lista = SolicitudVacaciones.objects.all()

	context =  {'lista': lista}
	return render(request, 'solicitudes/ver_sol_vacacion.html', context)

def aprobar(request, pk_solicitud):
    solicitud = get_object_or_404(SolicitudVacante, pk=pk_solicitud)
    if (request.method == 'POST'):
        form = SolFormV_aprobar(request.POST, instance = solicitud)
        if form.is_valid():
			#solicitud.aprobacion=1   //problema :S
            form.save()

            solicitud.save()

            return HttpResponseRedirect('/solicitudes/vervacante')
    else:
        formulario = SolFormV_aprobar(instance = solicitud)
    context =  {'solicitud': solicitud, 'formulario':formulario}
    return render(request, 'solicitudes/aprobar_solicitudVacante.html', context)
