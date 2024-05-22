from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponseServerError
from principalapp.forms import CustomUserCreationForm, UserUpdateForm, AddPropertyForm, UpdatePropertyForm, SearchPropertiesForm
from principalapp.models import Usuario, Inmueble, ImagenInmueble, Solicitud
from principalapp.backend.services import ArrendadorServices, ArrendatarioServices, NoLogService, UserService
from principalapp.backend.exceptions import RepositoryException, ServiceException
from principalapp.backend.repository import UserRepository

# Create your views here.
def inicio(request):  #SEPARADA EN CAPAS
    try:
        data = {
            'propiedades_aleatorias': NoLogService.get_muestra_inicio(),
            'mensaje': 'OK'
        }
        
    except ServiceException as se:
        data = {
            'propiedades_aleatorias': [],
            'mensaje': se.mensaje
        }
        return HttpResponseServerError(content=data['mensaje'])
    except Exception as e:
        data = {
            'propiedades_aleatorias': [],
            'mensaje': "Se ha producido un error inesperado"
        }
    return render(request=request, template_name="pages/welcome.html", context=data)




def registro(request): #SEPARADA EN CAPAS
    user_creation_form = UserService.registro(request)
    if user_creation_form is None:  # Si el formulario se guardó correctamente
        return redirect("/area_personal")
    
    return render(request=request, template_name="registration/register.html", context={'form': user_creation_form})



def personal_area(request): #SEPARADA EN CAPAS
    ruta_usuario = UserService.path_personal_area(user_django = request.user)
    return redirect(ruta_usuario)
    


def salir(request): #N/A
    logout(request)
    return redirect("/")


def user_data(request): #SEPARADA EN CAPAS
    data = UserRepository.get_usuario_app(request.user)
    return render(request,'registration/user_data.html',{'data':data} )


def update_profile(request): #SEPARADA EN CAPAS
    
    user_update_form = UserService.update_profile(request)
    if user_update_form is None:  # Si el formulario se guardó correctamente retorna none en el servicio
        return redirect("/mis_datos")
    
    return render(request=request, template_name="registration/update_profile.html", context= {"user_update_form": user_update_form})


def add_property(request): #SIN SEPARAR
    usuario_django = request.user
    usuario_app = Usuario.objects.get(user_ptr=usuario_django)
    arrendador_services = ArrendadorServices()
    if request.method == 'POST':
        add_property_form = AddPropertyForm(request.POST)
        if add_property_form.is_valid():
            propiedad = arrendador_services.publicar_propiedad(usuario_app, add_property_form)
            for file in request.FILES.getlist('imagenes'):
                ImagenInmueble.objects.create(propiedad=propiedad, imagen=file)
            
            return redirect("/mis_propiedades")
    
    add_property_form = AddPropertyForm()
    return render(request=request, template_name="pages/add_property.html", context={"add_property_form": add_property_form})


def my_properties(request):
    usuario_django = request.user
    usuario_app = Usuario.objects.get(user_ptr=usuario_django)
    arrendador_services = ArrendadorServices()
    
    
    propiedades = arrendador_services.listar_propiedades(usuario_app)
    
    
    
    return render(request=request, template_name="pages/my_properties.html", context={"propiedades": propiedades})


def update_properties(request, id_propiedad):
    usuario_django = request.user
    usuario_app = Usuario.objects.get(user_ptr=usuario_django)
    propiedad = Inmueble.objects.get(id=id_propiedad)
    arrendador_services = ArrendadorServices()
    
    if request.method == 'POST':
        update_property_form = UpdatePropertyForm(request.POST)
        if update_property_form.is_valid():
            arrendador_services.editar_propiedad(usuario_app, propiedad, update_property_form)
            return redirect("/mis_propiedades")
    
    initial_data = {
        'tipo_inmueble': propiedad.tipo_inmueble,
        'nombre': propiedad.nombre,
        'descripcion': propiedad.descripcion,
        'm2_construidos': propiedad.m2_construidos,
        'm2_totales': propiedad.m2_totales,
        'n_estacionamientos': propiedad.n_estacionamientos,
        'n_habitaciones': propiedad.n_habitaciones,
        'n_baños': propiedad.n_baños,
        'nombre_direccion': propiedad.direccion.nombre,
        'region': propiedad.direccion.comuna.region,
        'comuna': propiedad.direccion.comuna,
        'precio': propiedad.precio,
        'disponible': propiedad.disponible,
        }
    

    
    
    
    
    
    update_property_form = UpdatePropertyForm(initial=initial_data)
    return render(request=request, template_name="pages/update_property.html", context={"update_property_form": update_property_form, 'propiedad': propiedad})


def delete_property(request, id_propiedad):
    usuario_django = request.user
    usuario_app = Usuario.objects.get(user_ptr=usuario_django)
    propiedad = Inmueble.objects.get(id=id_propiedad)
    arrendador_services = ArrendadorServices()
    
    if request.method == 'POST':
        arrendador_services.eliminar_propiedad(usuario_app, propiedad)
        # messages.success(request, 'La propiedad ha sido eliminada correctamente.')
        return redirect("/mis_propiedades")
    
    else:
        return redirect("/mis_propiedades")
    
    
def search_properties(request):
    # arrendatario_services = ArrendatarioServices()
    # propiedades = arrendatario_services.listar_propiedades_comuna()
    
    if request.method == 'POST':
        search_properties_form = SearchPropertiesForm(request.POST)
        if search_properties_form.is_valid():
            arrendatario_services = ArrendatarioServices()
            propiedades = arrendatario_services.listar_propiedades(search_properties_form)
            return render(request, 'pages/search_properties.html', {'propiedades': propiedades, "search_properties_form": search_properties_form})
            

    
    search_properties_form = SearchPropertiesForm()
    return render(request=request, template_name="pages/search_properties.html", context={"search_properties_form": search_properties_form})


def view_property(request, id_propiedad):
    propiedad = Inmueble.objects.get(id=id_propiedad)
    if request.method == 'POST':
        return render(request=request, template_name="pages/view_property.html", context={"propiedad": propiedad})
    
    return render(request=request, template_name="pages/view_property.html", context={"propiedad": propiedad})
    
 
 
 
 
def request_property(request, id_propiedad):
    usuario_django = request.user
    usuario_app = Usuario.objects.get(user_ptr=usuario_django)
    propiedad = Inmueble.objects.get(id=id_propiedad)

    
    if request.method == 'POST':
        nueva_solicitud = Solicitud.objects.create(
            inmueble = propiedad,
            usuario = usuario_app
        )
        

        return redirect("/mis_solicitudes")
    
    else:
        return redirect("/mis_solicitudes")
    
    
def my_requests(request):
    usuario_django = request.user
    usuario_app = Usuario.objects.get(user_ptr=usuario_django)
    solicitudes = Solicitud.objects.filter(usuario = usuario_app)

    return render(request=request, template_name="pages/my_requests.html", context={"solicitudes": solicitudes})



def delete_request(request, solicitud_id):
    if request.method == 'POST':
        solicitud = Solicitud.objects.get(id=solicitud_id)
        solicitud.delete()
        # messages.success(request, 'Solicitud eliminada correctamente.')
        return redirect('/mis_solicitudes')
    else:
        # messages.error(request, 'La solicitud de eliminación debe realizarse a través de un formulario POST.')
        return redirect('/mis_solicitudes')
    
    
def my_requests_owner(request):
    usuario_django = request.user
    usuario_app = Usuario.objects.get(user_ptr=usuario_django)
    solicitudes = Solicitud.objects.filter(inmueble__usuarioinmueble__usuario=usuario_app, inmueble__usuarioinmueble__usuario__tipo_usuario__nombre='Arrendador')
    data = {
        'propietario': usuario_app,
        'solicitudes': solicitudes,
    }
    return render(request, 'pages/my_requests_owner.html', context=data)



def accept_request(request, solicitud_id):
    if request.method == 'POST':
        solicitud = Solicitud.objects.get(id=solicitud_id)
        solicitud.estado = "aceptada"
        solicitud.save()
        
        inmueble = solicitud.inmueble
        inmueble.disponible = False
        inmueble.save()
        
        # messages.success(request, 'Solicitud eliminada correctamente.')
        return redirect('/gestionar_solicitudes')
    else:
        # messages.error(request, 'La solicitud de eliminación debe realizarse a través de un formulario POST.')
        return redirect('/gestionar_solicitudes')
    
def reject_request(request, solicitud_id):
    if request.method == 'POST':
        solicitud = Solicitud.objects.get(id=solicitud_id)
        solicitud.estado = "rechazada"
        solicitud.save()
        # messages.success(request, 'Solicitud eliminada correctamente.')
        return redirect('/gestionar_solicitudes')
    else:
        # messages.error(request, 'La solicitud de eliminación debe realizarse a través de un formulario POST.')
        return redirect('/gestionar_solicitudes')


###########

   
    
    # if request.method == 'POST':
    #     update_property_form = UpdatePropertyForm(request.POST)
    #     if update_property_form.is_valid():
    #         arrendador_services.editar_propiedad(usuario_app, propiedad, update_property_form)
    #         return redirect("/mis_propiedades")
    
    
    # update_property_form = UpdatePropertyForm()
    # return render(request=request, template_name="pages/update_property.html", context={"update_property_form": update_property_form, 'propiedad': propiedad})


    # def listar_propiedades_comuna(self, comuna:Comuna):
    #     lista_propiedades = Inmueble.objects.filter(direccion__comuna = comuna, disponible = True)
    #     return lista_propiedades
    
    
    
    


