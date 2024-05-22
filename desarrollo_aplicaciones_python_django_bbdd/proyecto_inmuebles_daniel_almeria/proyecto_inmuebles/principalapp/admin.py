from django.contrib import admin
from principalapp.models import TipoInmueble, Inmueble, Region, Comuna, Direccion, TipoUsuario, Usuario, UsuarioInmueble, Solicitud, ImagenInmueble

# Register your models here.
admin.site.register(TipoInmueble)
admin.site.register(Inmueble)
admin.site.register(Region)
admin.site.register(Comuna)
admin.site.register(Direccion)
admin.site.register(TipoUsuario)
admin.site.register(Usuario)
admin.site.register(UsuarioInmueble)
admin.site.register(Solicitud)
admin.site.register(ImagenInmueble)
