from principalapp.models import Inmueble, Direccion, Usuario, UsuarioInmueble, Solicitud, TipoInmueble, Comuna, Region
from principalapp.backend.repository import NoLogRepository, UserRepository
from principalapp.backend.exceptions import RepositoryException, ServiceException
from principalapp.forms import CustomUserCreationForm, UserUpdateForm, AddPropertyForm, UpdatePropertyForm, SearchPropertiesForm
from django.contrib.auth import logout, authenticate, login
from django.shortcuts import redirect

class NoLogService:
    @staticmethod
    def get_muestra_inicio(max=10) -> list:
        try:
            return NoLogRepository.get_muestra_inicio()[:max]
        except RepositoryException as e:
            raise ServiceException(e.mensaje) 
        except Exception as e:
            raise ServiceException("Se ha producido un error en el servicio")
        
class UserService:
    @staticmethod
    def registro(request) -> CustomUserCreationForm:
        if request.method == "POST":
            user_creation_form = CustomUserCreationForm(data=request.POST)
        
            if user_creation_form.is_valid():
                UserRepository.registro(user_creation_form)
                
                #logeo automático al registrarse
                #authenticate devuelve un objeto User si las credenciales son correctas
                user = authenticate(username = user_creation_form.cleaned_data['username'], password = user_creation_form.cleaned_data['password1'])
                login(request, user)
                
                return None
        
        else:
            user_creation_form = CustomUserCreationForm()
            
        return user_creation_form
    
    @staticmethod
    def path_personal_area(user_django) -> str:
        usuario_app = UserRepository.get_usuario_app(user_django)
        
        if usuario_app.tipo_usuario.nombre.lower() == 'arrendador':
            return '/mis_propiedades'
        
        elif usuario_app.tipo_usuario.nombre.lower() == 'arrendatario':
            return '/buscar_propiedades'
        
        else:
            return '/admin'
        
        
    @staticmethod
    def update_profile(request) -> UserUpdateForm:
        usuario_app = UserRepository.get_usuario_app(request.user)
        
        if request.method == 'POST':
            user_update_form = UserUpdateForm(data=request.POST, instance=usuario_app)
            
            if user_update_form.is_valid():
                updated_data = user_update_form.cleaned_data
                UserRepository.update_profile(usuario_app, updated_data)
                return None
            
        user_update_form = UserUpdateForm(instance=usuario_app)
        
        return user_update_form     
        
     
        
        
            

class ArrendadorServices():
    
    def publicar_propiedad(self, usuario, formulario): #OPERATIVO
        
        nueva_direccion = Direccion.objects.create(
            nombre = formulario.cleaned_data['nombre_direccion'],
            comuna = formulario.cleaned_data['comuna']
            )
        
        nuevo_inmueble = Inmueble.objects.create(nombre = formulario.cleaned_data['nombre'],
                                                 descripcion = formulario.cleaned_data['descripcion'],
                                                 m2_construidos = formulario.cleaned_data['m2_construidos'],
                                                 m2_totales = formulario.cleaned_data['m2_totales'],
                                                 n_estacionamientos = formulario.cleaned_data['n_estacionamientos'],
                                                 n_habitaciones = formulario.cleaned_data['n_habitaciones'],
                                                 n_baños = formulario.cleaned_data['n_baños'],
                                                 precio = formulario.cleaned_data['precio'],
                                                 direccion = nueva_direccion,
                                                 tipo_inmueble = formulario.cleaned_data['tipo_inmueble'])
        
        UsuarioInmueble.objects.create(usuario = usuario,
                                       inmueble = nuevo_inmueble)
        
        return nuevo_inmueble
    
    
    
    
    # def publicar_propiedad(self, usuario: Usuario, nombre, descripcion, m2_construidos, m2_totales, n_estacionamientos, n_habitaciones, n_baños, precio, nombre_direccion, tipo_inmueble: TipoInmueble, comuna: Comuna):
        
    #     nueva_direccion = Direccion.objects.create(
    #         nombre = nombre_direccion,
    #         comuna = comuna
    #         )
        
    #     nuevo_inmueble = Inmueble.objects.create(nombre = nombre,
    #                                              descripcion = descripcion,
    #                                              m2_construidos = m2_construidos,
    #                                              m2_totales = m2_totales,
    #                                              n_estacionamientos = n_estacionamientos,
    #                                              n_habitaciones = n_habitaciones,
    #                                              n_baños = n_baños,
    #                                              precio = precio,
    #                                              direccion = nueva_direccion,
    #                                              tipo_inmueble = tipo_inmueble)
        
    #     UsuarioInmueble.objects.create(usuario = usuario,
    #                                    inmueble = nuevo_inmueble)
        
    #     return nuevo_inmueble
    
    
    
        
    def listar_propiedades(self, usuario: Usuario): #OPERATIVO
        lista_propiedades = UsuarioInmueble.objects.filter(usuario = usuario)
        return lista_propiedades
    
    def eliminar_propiedad(self, usuario: Usuario, inmueble: Inmueble): #OPERATIVO*
        if UsuarioInmueble.objects.filter(usuario=usuario, inmueble=inmueble).exists():
            UsuarioInmueble.objects.get(usuario = usuario, inmueble = inmueble).delete()
            return inmueble.delete()
        
        else:
            # Manejar el caso donde el usuario no tiene permisos para editar la propiedad
            # raise PermissionDenied("No tienes permiso para editar esta propiedad.")
            print('No tienes permiso para editar esta propiedad.')
    
    def editar_propiedad(self, usuario: Usuario, inmueble: Inmueble, formulario): #OPERATIVO
        
        # Verificar si el inmueble pertenece al usuario antes de editar
        if UsuarioInmueble.objects.filter(usuario=usuario, inmueble=inmueble).exists():
            
            # Actualizar los atributos del inmueble
            inmueble.nombre = formulario.cleaned_data['nombre']
            inmueble.descripcion = formulario.cleaned_data['descripcion']
            inmueble.m2_construidos = formulario.cleaned_data['m2_construidos']
            inmueble.m2_totales = formulario.cleaned_data['m2_totales']
            inmueble.n_estacionamientos = formulario.cleaned_data['n_estacionamientos']
            inmueble.n_habitaciones = formulario.cleaned_data['n_habitaciones']
            inmueble.n_baños = formulario.cleaned_data['n_baños']
            inmueble.tipo_inmueble = formulario.cleaned_data['tipo_inmueble']
            inmueble.precio = formulario.cleaned_data['precio']
            inmueble.disponible = formulario.cleaned_data['disponible']
            inmueble.save()

            # Actualizar la dirección del inmueble
            inmueble.direccion.nombre = formulario.cleaned_data['nombre_direccion']
            inmueble.direccion.comuna = formulario.cleaned_data['comuna']
            inmueble.direccion.save()

            return inmueble
        else:
            # Manejar el caso donde el usuario no tiene permisos para editar la propiedad
            # raise PermissionDenied("No tienes permiso para editar esta propiedad.")
            print('No tienes permiso para editar esta propiedad.')
            
            
    # def editar_propiedad(self, usuario: Usuario, inmueble: Inmueble, nombre, descripcion, m2_construidos, m2_totales, n_estacionamientos, n_habitaciones, n_baños, tipo_inmueble:TipoInmueble , precio, disponible, nombre_direccion, comuna: Comuna):
        
    #     # Verificar si el inmueble pertenece al usuario antes de editar
    #     if UsuarioInmueble.objects.filter(usuario=usuario, inmueble=inmueble).exists():
            
    #         # Actualizar los atributos del inmueble
    #         inmueble.nombre = nombre
    #         inmueble.descripcion = descripcion
    #         inmueble.m2_construidos = m2_construidos
    #         inmueble.m2_totales = m2_totales
    #         inmueble.n_estacionamientos = n_estacionamientos
    #         inmueble.n_habitaciones = n_habitaciones
    #         inmueble.n_baños = n_baños
    #         inmueble.tipo_inmueble = tipo_inmueble
    #         inmueble.precio = precio
    #         inmueble.disponible = disponible
    #         inmueble.save()

    #         # Actualizar la dirección del inmueble
    #         inmueble.direccion.nombre = nombre_direccion
    #         inmueble.direccion.comuna = comuna
    #         inmueble.direccion.save()

    #         return inmueble
    #     else:
    #         # Manejar el caso donde el usuario no tiene permisos para editar la propiedad
    #         # raise PermissionDenied("No tienes permiso para editar esta propiedad.")
    #         print('No tienes permiso para editar esta propiedad.')
            
    def aceptar_arrendatario(self, solicitud: Solicitud, eleccion):
        if eleccion == 'aceptar':
            solicitud.estado = 'aceptada'
            solicitud.save()
            solicitud.inmueble.disponible = False
            solicitud.inmueble.save()
            return solicitud
        else:
            solicitud.estado = 'rechazada'
        
        
class ArrendatarioServices():
    
    def listar_propiedades(self, formulario):   #OPERATIVO
        tipo_inmueble = formulario.cleaned_data['tipo_inmueble']
        region = formulario.cleaned_data['region']
        comuna = formulario.cleaned_data['comuna']
        disponible = formulario.cleaned_data['disponible']
        
        queryset = Inmueble.objects.all()
        
        # Filtrar por tipo de inmueble si se selecciona algo diferente a "Todos"
        if tipo_inmueble and tipo_inmueble != 'Todos':
            queryset = queryset.filter(tipo_inmueble=tipo_inmueble)

        # Filtrar por región si se selecciona algo diferente a "Todos"
        if region and region != 'Todos':
            queryset = queryset.filter(direccion__comuna__region = region)

        # Filtrar por comuna si se selecciona algo diferente a "Todos"
        if comuna and comuna != 'Todos':
            queryset = queryset.filter(direccion__comuna=comuna)
            
        if disponible == True:
            queryset = queryset.filter(disponible=disponible)
            
        # Retornar el queryset filtrado
        return queryset
        
        
        
        
        
    
    
    # def listar_propiedades_comuna(self, comuna:Comuna):
    #     lista_propiedades = Inmueble.objects.filter(direccion__comuna = comuna, disponible = True)
    #     return lista_propiedades
    
    # def listar_propiedades_region(self, region:Region):
    #     lista_propiedades = Inmueble.objects.filter(direccion__comuna__region = region, disponible = True)
    #     return lista_propiedades
    
    def solicitar_arriendo(self, inmueble:Inmueble, usuario: Usuario):
        nueva_solicitud = Solicitud.objects.create(inmueble = inmueble, usuario = usuario)
        return nueva_solicitud



