from principalapp.models import Inmueble
from django.db.models import QuerySet
from principalapp.backend.exceptions import RepositoryException
from principalapp.models import Usuario


class NoLogRepository:
    @staticmethod
    def get_muestra_inicio() -> QuerySet:
        try: 
            return Inmueble.objects.order_by('?')
        except Exception as e:
            raise RepositoryException("Error al obtener los datos")
        

class UserRepository:
    @staticmethod
    def registro(user_creation_form):
        user_creation_form.save()
        
    @staticmethod
    def get_usuario_app(user_django) -> Usuario:
        return Usuario.objects.get(user_ptr=user_django)
    
    @staticmethod
    def update_profile(usuario_app, data):
        usuario_app.first_name = data['first_name']
        usuario_app.last_name = data['last_name']
        usuario_app.email = data['email']
        usuario_app.direccion = data['direccion']
        usuario_app.telefono = data['telefono']
        usuario_app.tipo_usuario = data['tipo_usuario']
        usuario_app.save()
        

# class ArrendadorRepository:
#     @staticmethod
#     add_property()
        
        
        
        
