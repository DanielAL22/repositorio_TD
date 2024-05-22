from django.test import TestCase
from proyecto_inmuebles.principalapp.backend.services import ArrendadorServices, ArrendatarioServices
from principalapp.models import Inmueble, Direccion, Usuario, UsuarioInmueble, Solicitud, TipoInmueble, TipoUsuario, Region, Comuna, Direccion


def creacion_tipo_usuario_setup():
    tipo_usuario1 = TipoUsuario.objects.create(
        nombre = 'arrendador'
    )
    tipo_usuario2 = TipoUsuario.objects.create(
        nombre = 'arrendatario'
    )
    
    return tipo_usuario1, tipo_usuario2

def creacion_tipo_inmueble_setup():
    tipo_inmueble = TipoInmueble.objects.create(
        nombre = 'departamento'
    )
    
    return tipo_inmueble

def creacion_region_setup():
    region = Region.objects.create(
        nombre = 'Metropolitana'
    )
    
    return region

def creacion_comuna_setup(region):
    comuna1 = Comuna.objects.create(
        nombre = 'Ñuñoa',
        region = region
    )
    
    comuna2 = Comuna.objects.create(
        nombre = 'Macul',
        region = region
    )
    
    return comuna1, comuna2

def creacion_direccion_setup(comuna1, comuna2):
    direccion1 = Direccion.objects.create(
        nombre = 'Holanda 77',
        comuna = comuna1
    )
    
    direccion2 = Direccion.objects.create(
        nombre = 'calle 555', comuna = comuna2
        )
    
    return direccion1, direccion2
    
    
    
    
def creacion_usuarios_setup(tipo_usuario1, tipo_usuario2) -> Usuario:
    new_usuario_arrendador = Usuario.objects.create(nombres = 'Daniel',
                                                    apellidos = 'Almería',
                                                    rut = '1-1',
                                                    direccion = 'av la florida 77',
                                                    telefono = '9999',
                                                    email = 'd@b.com',
                                                    tipo_usuario = tipo_usuario1)
    
    new_usuario_arrendatario = Usuario.objects.create(nombres = 'Consuelo',
                                                    apellidos = 'Fredericksen',
                                                    rut = '1-2',
                                                    direccion = 'holanda 88',
                                                    telefono = '11111',
                                                    email = 'c@d.com',
                                                    tipo_usuario = tipo_usuario2)
    
    
    return new_usuario_arrendador, new_usuario_arrendatario

def creacion_inmuebles_setup(tipo_inmueble1, direccion1, direccion2) -> Inmueble:
    new_inmueble1 = Inmueble.objects.create(nombre='Mi casa',
                                            descripcion='Una casa bonita',
                                            m2_construidos=150,
                                            m2_totales=200,
                                            n_estacionamientos=2,
                                            n_habitaciones=3,
                                            n_baños=2,
                                            tipo_inmueble=tipo_inmueble1,  # Aquí usamos el valor correspondiente a 'dpto'
                                            precio=250000,
                                            direccion = direccion1)
    
    
    
    new_inmueble2 = Inmueble.objects.create(nombre='Mi casa2',
                                            descripcion='Otra casa bonita',
                                            m2_construidos=150,
                                            m2_totales=200,
                                            n_estacionamientos=2,
                                            n_habitaciones=3,
                                            n_baños=2,
                                            tipo_inmueble=tipo_inmueble1,  # Aquí usamos el valor correspondiente a 'dpto'
                                            precio=250000,
                                            disponible=False,
                                            direccion = direccion2)
    
    
    return new_inmueble1, new_inmueble2


def creacion_usuario_inmueble_setup(new_usuario, new_inmueble1, new_inmueble2) -> UsuarioInmueble:
    usuario_inmueble1 = UsuarioInmueble.objects.create(
        usuario = new_usuario,
        inmueble = new_inmueble1
    )
    
    usuario_inmueble2 = UsuarioInmueble.objects.create(
        usuario = new_usuario,
        inmueble = new_inmueble2
    )
    
    return usuario_inmueble1, usuario_inmueble2

def creacion_solicitud_setup(usuario, inmueble) -> Solicitud:
    solicitud = Solicitud.objects.create(
        usuario = usuario,
        inmueble = inmueble
    )
    
    return solicitud


    

    

# Create your tests here.
class ArrendadorServicesTest(TestCase):
    def setUp(self) -> None:
        print('setup ArrendadorServicesTest')
        new_region = creacion_region_setup()
        new_comuna1, new_comuna2 = creacion_comuna_setup(new_region)
        new_direccion1, new_direccion2 = creacion_direccion_setup(new_comuna1, new_comuna2)
        tipo_usuario1, tipo_usuario2 = creacion_tipo_usuario_setup()
        new_usuario_arrendador, new_usuario_arrendatario = creacion_usuarios_setup(tipo_usuario1, tipo_usuario2)
        tipo_inmueble1 = creacion_tipo_inmueble_setup()
        new_inmueble1, new_inmueble2 = creacion_inmuebles_setup(tipo_inmueble1, new_direccion1, new_direccion2)
        usuario_inmueble1, usuario_inmueble2 = creacion_usuario_inmueble_setup(new_usuario_arrendador, new_inmueble1, new_inmueble2)
        solicitud1 = creacion_solicitud_setup(new_usuario_arrendatario, new_inmueble1)
        
        

    
    def test_publicar_propiedad(self):
        print('test_publicar_propiedad')
        usuario = Usuario.objects.get(rut = '1-1')
        tipo_inmueble = TipoInmueble.objects.get(nombre = 'departamento')
        comuna = Comuna.objects.get(nombre = 'Ñuñoa')
        arrendador_services = ArrendadorServices()
        prueba = arrendador_services.publicar_propiedad(usuario = usuario,
                                                       nombre='Mi casa',
                                                      descripcion='Una casa bonita',
                                                      m2_construidos=150,
                                                      m2_totales=200,
                                                      n_estacionamientos=2,
                                                      n_habitaciones=3,
                                                      n_baños=2,
                                                      precio=250000,
                                                      nombre_direccion = 'Holanda 88',
                                                      tipo_inmueble=tipo_inmueble,
                                                      comuna = comuna
                                                      )
        
        
        print(type(prueba))
        print(prueba)
        self.assertTrue(prueba)
        self.assertIsInstance(prueba, Inmueble)
        
        
        
    def test_listar_propiedades(self):
        print('test_listar_propiedades')
        usuario = Usuario.objects.get(rut = '1-1')
        arrendador_services = ArrendadorServices()
        prueba = arrendador_services.listar_propiedades(usuario=usuario)
        
        print(prueba)
        print(type(prueba))
        self.assertTrue(prueba)
        for propiedad in prueba:
            print(propiedad)
            self.assertIsInstance(propiedad, UsuarioInmueble)
            
            
            
    def test_eliminar_propiedad(self):
        print('test_eliminar_propiedad')
        
        print('ANTES')
        inmuebles = Inmueble.objects.all()
        for i in inmuebles:
            print(i)
            
        usuarios_inmuebles = UsuarioInmueble.objects.all()
        for ui in usuarios_inmuebles:
            print(ui)
            
            
        
        usuario = Usuario.objects.get(rut = '1-1')
        inmueble = Inmueble.objects.get(nombre = 'Mi casa')
        print(usuario)
        print(inmueble)
        arrendador_services = ArrendadorServices()
        prueba = arrendador_services.eliminar_propiedad(usuario=usuario, inmueble = inmueble)
        
        
        print('DESPUES')
        inmuebles = Inmueble.objects.all()
        for i in inmuebles:
            print(i)
            
        usuarios_inmuebles = UsuarioInmueble.objects.all()
        for ui in usuarios_inmuebles:
            print(ui)
        
        
        # print(prueba)
        # self.assertEqual(UsuarioInmueble.objects.filter(usuario=usuario, inmueble=inmueble).count(), 0)
        # self.assertEqual(Inmueble.objects.filter(nombre = 'Mi casa').count(), 0)
        
        
        
    def test_editar_propiedad(self):
        print('test_editar_propiedad')
        usuario = Usuario.objects.get(rut = '1-1')
        inmueble = Inmueble.objects.get(nombre = 'Mi casa')
        comuna = Comuna.objects.get(nombre = 'Macul')
        tipo_inmueble = TipoInmueble.objects.get(nombre = 'departamento')
        
        arrendador_services = ArrendadorServices()
        prueba = arrendador_services.editar_propiedad(usuario = usuario, 
                                                      inmueble = inmueble,
                                                      nombre='Mi casa modificada', 
                                                      descripcion='Una casa bonita modificada', 
                                                      m2_construidos=150, 
                                                      m2_totales=200, 
                                                      n_estacionamientos=2, 
                                                      n_habitaciones=3, 
                                                      n_baños=2, 
                                                      tipo_inmueble=tipo_inmueble,  
                                                      precio=300000, 
                                                      disponible=True,
                                                      nombre_direccion='calle 333', 
                                                      comuna=comuna)

        print(prueba)
        inmuebles = Inmueble.objects.all()
        for i in inmuebles:
            print(i)
            
            
    def test_aceptar_arrendatario(self):
        print('test_aceptar_arrendatario')
        usuario = Usuario.objects.get(rut = '1-2')
        inmueble = Inmueble.objects.get(nombre = 'Mi casa')
        solicitud = Solicitud.objects.create(usuario = usuario, inmueble = inmueble)
        arrendador_services = ArrendadorServices()
        prueba = arrendador_services.aceptar_arrendatario(solicitud = solicitud, eleccion = 'aceptar')
        print(prueba)
        
    
    

class ArrendatarioServicesTest(TestCase):
    def setUp(self) -> None:
        print('setup ArrendatarioServicesTest')
        new_region = creacion_region_setup()
        new_comuna1, new_comuna2 = creacion_comuna_setup(new_region)
        new_direccion1, new_direccion2 = creacion_direccion_setup(new_comuna1, new_comuna2)
        tipo_usuario1, tipo_usuario2 = creacion_tipo_usuario_setup()
        new_usuario_arrendador, new_usuario_arrendatario = creacion_usuarios_setup(tipo_usuario1, tipo_usuario2)
        tipo_inmueble1 = creacion_tipo_inmueble_setup()
        new_inmueble1, new_inmueble2 = creacion_inmuebles_setup(tipo_inmueble1, new_direccion1, new_direccion2)
        usuario_inmueble1, usuario_inmueble2 = creacion_usuario_inmueble_setup(new_usuario_arrendador, new_inmueble1, new_inmueble2)
        solicitud1 = creacion_solicitud_setup(new_usuario_arrendatario, new_inmueble1)
        
    def test_listar_propiedades_comuna(self):
        print('test_listar_propiedades_comuna')
        arrendatario_services = ArrendatarioServices()
        comuna = Comuna.objects.get(nombre = 'Ñuñoa')
        prueba = arrendatario_services.listar_propiedades_comuna(comuna=comuna)
        
        
        #requerimiento2
        datos_propiedades_comuna = open('datos_propiedades_comuna.txt', 'a', encoding='utf-8')
        for i, propiedad in enumerate(prueba):
            datos_propiedades_comuna.write(f"Propiedad: {i+1}, ")
            datos_propiedades_comuna.write(f"Nombre: {propiedad.nombre}, ")
            datos_propiedades_comuna.write(f"Descripción: {propiedad.descripcion}")
            datos_propiedades_comuna.write(f"\n")
        
        print(prueba)
        print(type(prueba))
        # self.assertTrue(prueba)
        for propiedad in prueba:
            print(propiedad)
            self.assertIsInstance(propiedad, Inmueble)
            
    def test_listar_propiedades_region(self):
        print('test_listar_propiedades_region')
        arrendatario_services = ArrendatarioServices()
        region = Region.objects.get(nombre = 'Metropolitana')
        prueba = arrendatario_services.listar_propiedades_region(region=region)
        
        
        #requerimiento3
        datos_propiedades_region = open('datos_propiedades_region.txt', 'a', encoding='utf-8')
        for i, propiedad in enumerate(prueba):
            datos_propiedades_region.write(f"Propiedad: {i+1}, ")
            datos_propiedades_region.write(f"Nombre: {propiedad.nombre}, ")
            datos_propiedades_region.write(f"Descripción: {propiedad.descripcion}")
            datos_propiedades_region.write(f"\n")
        
        print(prueba)
        print(type(prueba))
        # self.assertTrue(prueba)
        for propiedad in prueba:
            print(propiedad)
            self.assertIsInstance(propiedad, Inmueble)

            
   
    def test_solicitar_arriendo(self):
        print('test_solicitar_arriendo')
        
        usuario = Usuario.objects.get(rut = '1-1')
        inmueble = Inmueble.objects.get(nombre = 'Mi casa')
        
        arrendatario_services = ArrendatarioServices()
        prueba = arrendatario_services.solicitar_arriendo(usuario=usuario, inmueble=inmueble)
        print(prueba)
    