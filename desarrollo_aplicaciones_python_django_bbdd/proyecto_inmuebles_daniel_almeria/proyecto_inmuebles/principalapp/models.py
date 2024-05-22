from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



 
 
class TipoInmueble(models.Model):
    # TIPOS_INMUEBLE = (
    #     ('casa', 'casa'),
    #     ('departamento', 'departamento'),
    #     ('parcela', 'parcela')
    #     )

    # nombre = models.CharField(max_length=12, choices=TIPOS_INMUEBLE)
    nombre = models.CharField(max_length=12)
    def __str__(self):
        return f"{self.nombre}"  
    
class Region(models.Model):
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.nombre}" 
    
class Comuna(models.Model):
    nombre = models.CharField(max_length=50)
    region = models.ForeignKey(to=Region, on_delete=models.PROTECT)
    def __str__(self):
        return f"{self.nombre}" 

class Direccion(models.Model):
    nombre = models.CharField(max_length=100)
    comuna = models.ForeignKey(to = Comuna, on_delete=models.PROTECT)
    
    def __str__(self):
        return f"[{self.nombre} - {self.comuna.nombre}]"
     
class Inmueble(models.Model):

    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    m2_construidos = models.IntegerField()
    m2_totales = models.IntegerField()
    n_estacionamientos = models.IntegerField()
    n_habitaciones = models.IntegerField()
    n_baños = models.IntegerField()
    precio = models.IntegerField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    direccion = models.OneToOneField(Direccion, on_delete=models.CASCADE)
    disponible = models.BooleanField(default=True)
    tipo_inmueble = models.ForeignKey(TipoInmueble, on_delete=models.PROTECT)
    
    def __str__(self):
        return f"[{self.nombre} - {self.direccion} - {self.disponible}]"    
    

class ImagenInmueble(models.Model):
    propiedad = models.ForeignKey(Inmueble, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='propiedades/')
  
    
class TipoUsuario(models.Model):
    # TIPOS_USUARIO = (
    #     (1, 'arrendador'),
    #     (2, 'arrendatario')
    #     )
    # nombre = models.CharField(max_length=12, choices=TIPOS_USUARIO)
    nombre = models.CharField(max_length=12)
    def __str__(self):
        return f"{self.nombre}" 

class Usuario(User):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    rut = models.CharField(max_length=9, unique=True)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=9, unique=True)
    tipo_usuario = models.ForeignKey(to=TipoUsuario, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"[{self.rut}]"

    
    
    
class UsuarioInmueble(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT) #no se podrá eliminar el principal (usuario) si tiene inmuebles relacionados
    inmueble = models.ForeignKey(Inmueble, on_delete=models.PROTECT) #no se podrá eliminar el principal (inmueble) si tiene usuarios relacionados
    fecha_inicio = models.DateField(null=True, blank=True)  #nulable porque se supone que cuando el usuario es arrendador irá vacío
    fecha_fin = models.DateField(null=True, blank=True) #nulable porque se supone que cuando el usuario es arrendador irá vacío
    
    def __str__(self):
        return f"[{self.usuario.rut} - {self.inmueble.nombre}]"
    
    
class Solicitud(models.Model):
    # ESTADOS_SOLICITUD = (
    #     (1, 'en espera'),
    #     (2, 'aceptada'),
    #     (3, 'rechazada')
    # )
    
    inmueble = models.ForeignKey(Inmueble, on_delete=models.CASCADE) #si se elimina el inmueble se eliminaran las solicitudes asociadas
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE) #si se elimina el usuario se eliminaran las solicitudes asociadas
    # estado = models.CharField(max_length=9, choices=ESTADOS_SOLICITUD, default='en espera')
    estado = models.CharField(max_length=9, default='en espera')
    
    def __str__(self):
        return f"[{self.usuario.rut} - {self.usuario.rut} - {self.inmueble.nombre}]"
    

    

