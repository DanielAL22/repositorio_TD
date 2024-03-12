from encuesta import Encuesta
from listado_respuestas import ListadoRespuestas


class Usuario:
    def __init__(self, correo:str, edad:int, region:int) -> None:
        self.__correo = correo
        self.__edad = edad
        self.__region = region

    @property
    def correo(self) -> int:
        return self.__correo

    @correo.setter
    def correo(self, valor: int) -> None:
        self.__correo = valor

    @property
    def edad(self) -> int:
        return self.__edad

    @edad.setter
    def edad(self, valor: int) -> None:
        self.__edad = valor


    @property
    def region(self) -> int:
        return self.__region

    @region.setter
    def region(self, valor: int) -> None:
        self.__region = valor





    def contestar_encuesta(self, nombre_encuesta, lista_preguntas):
        encuesta = Encuesta(nombre_encuesta, lista_preguntas)