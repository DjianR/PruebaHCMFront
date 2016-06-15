from django.conf.urls import include, url
from django.contrib import admin
from solicitudes import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'Prueba_HCMFront.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)), #urls del admin
    url(r'^solicitudes/', include('solicitudes.urls', namespace="solicitudes")),


    #url(r'^vacaciones$', views.SolicitudVacaciones, name='vacaciones'),


]
