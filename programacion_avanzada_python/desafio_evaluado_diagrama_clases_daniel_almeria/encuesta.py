from pregunta import Pregunta
from listado_respuestas import ListadoRespuestas

class Encuesta:
    def __init__(self, nombre:str, lista_preguntas:list) -> None:
        self.nombre = nombre
        self.__lista_preguntas = lista_preguntas
        self.__lista_lista_respuestas = []


    def mostrar_encuesta(self):
        print(self.nombre)
        for pregunta in self.__lista_preguntas:
            pregunta.mostrar_pregunta()

    def add_lista_respuestas(self, respuestas):
        pass

class EncuestaEdad(Encuesta):
    def __init__(self, nombre: str, lista_preguntas: list, lista_lista_respuestas: list, edad_min:int, edad_max:int) -> None:
        super().__init__(nombre, lista_preguntas, lista_lista_respuestas)
        self.edad_min = edad_min
        self.edad_max = edad_max

    @property
    def edad_min(self) -> int:
        return self.__edad_min

    @edad_min.setter
    def edad_min(self, valor: int) -> None:
        self.__edad_min = valor
    
    
    @property
    def edad_max(self) -> int:
        return self.__edad_max

    @edad_max.setter
    def edad_max(self, valor: int) -> None:
        self.__edad_max = valor

    #sobreescritura
    def add_lista_respuestas(self):
        pass


class EncuestaRegion(Encuesta):
    def __init__(self, nombre: str, lista_preguntas: list, lista_lista_respuestas: list, lista_regiones:list) -> None:
        super().__init__(nombre, lista_preguntas, lista_lista_respuestas)
        self.__lista_regiones = lista_regiones

    @property
    def lista_regiones(self) -> int:
        return self.__lista_regiones

    @lista_regiones.setter
    def lista_regiones(self, valor: int) -> None:
        self.__lista_regiones = valor

    #sobreescritura
    def add_lista_respuestas(self):
        pass



