from usuario import Usuario

class ListadoRespuestas:
    def __init__(self, usuario:Usuario, lista_respuestas:list) -> None:
        self.__usuario = usuario
        self.__lista_respuestas = lista_respuestas

    @property
    def usuario(self) -> str:
        return self.__usuario

    @property
    def lista_respuestas(self) -> list:
        return self.__lista_respuestas