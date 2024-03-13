# 1. En un archivo membresia.py, crear la clase que permita definir los atributos de instancia y comportamiento de todas las membresías. Considere:
# (2 Puntos)
# a. Utilice abstracción para definir el o los comportamientos requeridos (puede definir también métodos no abstractos).
# b. Utilice encapsulamiento para los atributos de instancia. Declare las propiedades que estime necesarias según lo solicitado.


from abc import ABC, abstractmethod
class Membresia (ABC):
    def __init__(self, correo_electronico: str, n_tarjeta: str) -> None:
        super().__init__()
        self.__correo_electronico = correo_electronico
        self.__n_tarjeta = n_tarjeta

    @property
    def correo_electronico(self):
        return self.__correo_electronico

    @property
    def n_tarjeta(self):
        return self.__n_tarjeta


    @abstractmethod
    def cambiar_suscripcion(self, id_membresia: int):
        if id_membresia == 1:
            print("Has cambiado a membresía Básica")
            nueva_membresia = MembresiaBasica(self.correo_electronico, self.n_tarjeta)
        elif id_membresia == 2:
            print("Has cambiado a membresía Familiar")
            nueva_membresia = MembresiaFamiliar(self.correo_electronico, self.n_tarjeta)
        elif id_membresia == 3:
            print("Has cambiado a membresía Sin Conexión")
            nueva_membresia = MembresiaSinConexion(self.correo_electronico, self.n_tarjeta)
        else:
            print("Has cambiado a membresía Pro")
            nueva_membresia = MembresiaPro(self.correo_electronico, self.n_tarjeta)

        return nueva_membresia



class MembresiaGratis(Membresia):
    COSTO = 0
    DISPOSITIVOS = 1

    def __init__(self, correo_electronico: str, n_tarjeta: str) -> None:
        super().__init__(correo_electronico, n_tarjeta)


    def cambiar_suscripcion(self, id_membresia: int):
        if id_membresia not in [1, 2, 3, 4]:
            print("Su membresía sigue siendo Gratis")
            return self
        else:
            return super().cambiar_suscripcion(id_membresia)

class MembresiaBasica(Membresia):
    COSTO = 3000
    DISPOSITIVOS = 2

    def __init__(self, correo_electronico: str, n_tarjeta: str) -> None:
        super().__init__(correo_electronico, n_tarjeta)


    def cambiar_suscripcion(self, id_membresia: int):
        if id_membresia not in [2, 3, 4]:
            print("Su membresía sigue siendo Básica")
            return self
        else:
            return super().cambiar_suscripcion(id_membresia)

    def cancelar_suscripcion(self):
        print("Has cancelado tu suscripción. Su nueva membresía es Gratis")
        nueva_membresia = MembresiaGratis(self.correo_electronico, self.n_tarjeta)
        return nueva_membresia


class MembresiaFamiliar(MembresiaBasica):
    COSTO = 5000
    DISPOSITIVOS = 5

    def __init__(self, correo_electronico: str, n_tarjeta: str) -> None:
        super().__init__(correo_electronico, n_tarjeta)
        self.dias_regalo = 7


    def cambiar_suscripcion(self, id_membresia: int):
        if id_membresia not in [1, 3, 4]:
            print("Su membresía sigue siendo Familiar")
            return self
        else:
            return super().cambiar_suscripcion(id_membresia)

    def control_parental(self):
        pass


class MembresiaSinConexion(MembresiaBasica):
    COSTO = 3500
    DISPOSITIVOS = 2

    def __init__(self, correo_electronico: str, n_tarjeta: str) -> None:
        super().__init__(correo_electronico, n_tarjeta)
        self.dias_regalo = 7


    def cambiar_suscripcion(self, id_membresia: int):
        if id_membresia not in [1, 2, 4]:
            print("Su membresía sigue siendo Sin Conexión")
            return self
        else:
            return super().cambiar_suscripcion(id_membresia)

    def incrementar_contenido(self):
        pass



class MembresiaPro(MembresiaFamiliar, MembresiaSinConexion):  #HERENCIA MÚLTIPLE
    COSTO = 7000
    DISPOSITIVOS = 6

    def __init__(self, correo_electronico: str, n_tarjeta: str) -> None:
        super().__init__(correo_electronico, n_tarjeta)
        self.dias_regalo = 15


    def cambiar_suscripcion(self, id_membresia: int):
        if id_membresia not in [1, 2, 3]:
            print("Su membresía sigue siendo Pro")
            return self
        else:
            return super().cambiar_suscripcion(id_membresia)


        

m = MembresiaGratis("pepito@gmail.com", "11223344")
print(type(m))

nueva_membresia = m.cambiar_suscripcion(1)
print(type(nueva_membresia))

nueva_membresia2 = nueva_membresia.cambiar_suscripcion(3)
print(type(nueva_membresia2))

nueva_membresia3 = nueva_membresia2.cancelar_suscripcion()
print(type(nueva_membresia3))

