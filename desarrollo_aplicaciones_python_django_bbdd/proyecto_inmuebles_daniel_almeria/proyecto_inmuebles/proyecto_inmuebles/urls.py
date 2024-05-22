"""
URL configuration for proyecto_inmuebles project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from principalapp.views import inicio, registro, salir, user_data, update_profile, add_property, my_properties, update_properties, delete_property, search_properties, personal_area, view_property, my_requests, request_property, delete_request, my_requests_owner, accept_request, reject_request
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')), #urls de django para autenticacion
    path('', inicio, name = 'inicio'),
    path('registro/', registro, name = 'registro'),
    path('salir/', salir, name='salir'),
    path('mis_datos/', user_data, name='user_data'),
    path('actualizar_datos/', update_profile, name='update_profile'),
    path('publicar_propiedad/', add_property, name='add_property'),
    path('mis_propiedades/', my_properties, name='my_properties'),
    path('editar_propiedad/<int:id_propiedad>/', update_properties, name='update_properties'),
    path('eliminar_propiedad/<int:id_propiedad>/', delete_property, name='delete_property'),
    path('buscar_propiedades/', search_properties, name='search_properties'),
    path('area_personal/', personal_area, name='personal_area'),
    path('ver_detalle/<int:id_propiedad>/', view_property, name='view_property'),
    path('solicitar_propiedad/<int:id_propiedad>/', request_property, name='request_property'),
    path('mis_solicitudes/', my_requests, name='my_requests'),
    path('eliminar_solicitud/<int:solicitud_id>/', delete_request, name='delete_request'),
    path('gestionar_solicitudes/', my_requests_owner, name='my_requests_owner'),
    path('aceptar_solicitud/<int:solicitud_id>/', accept_request, name='accept_request'),
    path('rechazar_solicitud/<int:solicitud_id>/', reject_request, name='reject_request'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
