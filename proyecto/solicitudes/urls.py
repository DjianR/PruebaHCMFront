from django.conf.urls import include, url
from django.contrib import admin
from solicitudes import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'Prueba_HCMFront.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^empleado$', views.empleado, name='empleado'),
    url(r'^encargado$', views.encargadoRRHH, name='encargado'),
    url(r'^vacante$', views.nuevaVacante, name='vacantes'),
    url(r'^vacaciones$', views.nuevaVacacion, name='vacaciones'),
    url(r'^vervacante$', views.verVacante, name='vervacantes'),
    url(r'^vervacaciones$', views.verVacacion, name='vervacaciones'),
    url(r'^$', views.inicio, name='inicio'),

    url(r'^(?P<pk_solicitud>\d+)/$', views.aprobar, name='aprobar'),

]
