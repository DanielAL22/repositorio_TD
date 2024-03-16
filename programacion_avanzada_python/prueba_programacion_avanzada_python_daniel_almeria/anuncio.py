from abc import ABC, abstractmethod, abstractclassmethod
from error import SubTipoInvalidoError

class Anuncio(ABC):
    def __init__(self, ancho: int, alto: int, url_archivo: str, url_click: str, sub_tipo: str) -> None:
        self.__ancho = ancho if ancho > 0 else 1
        self.__alto = alto if alto > 0 else 1
        self.__url_archivo = url_archivo
        self.__url_click = url_click
        self.__sub_tipo = sub_tipo

    @property
    def ancho(self):
        return self.__ancho

    @ancho.setter
    def ancho(self, valor: int):
        self.__ancho = valor if valor > 0 else 1

    @property
    def alto(self) -> int:
        return self.__alto

    @alto.setter
    def alto(self, valor: int):
        self.__alto = valor if valor > 0 else 1

    @property
    def url_archivo(self):
        return self.__url_archivo

    @url_archivo.setter
    def url_archivo(self, valor: str):
        self.__url_archivo = valor

    @property
    def url_click(self):
        return self.__url_click

    @url_click.setter
    def url_click(self, valor: str):
        self.__url_click = valor

    @property
    def sub_tipo(self):
        return self.__sub_tipo

    @sub_tipo.setter
    def sub_tipo(self, valor: str):
        if valor in self.SUB_TIPOS:
            self.__sub_tipo = valor
        else:
            raise SubTipoInvalidoError("El subtipo de formato introducido no es válido")

    @abstractclassmethod
    def mostrar_formatos(cls):
        print(f"""
        FORMATO {cls.FORMATO}
        =================
        -Subtipo {cls.SUB_TIPOS[0]}
        -Subtipo {cls.SUB_TIPOS[1]}
        """)
    
    
    @abstractmethod
    def comprimir_anuncio():
        pass

    def redimensionar_anuncio():
        pass

class Video(Anuncio):
    FORMATO = "Video"
    SUB_TIPOS = ("instream", "outstream")
    def __init__(self, url_archivo: str, url_click: str, sub_tipo: str, duracion: int) -> None:
        super().__init__(1, 1,  url_archivo, url_click, sub_tipo) # Ancho y alto fijos para la clase Video
        self.__duracion = duracion if duracion > 0 else 5

    @property
    def duracion(self):
        return self.__duracion

    @duracion.setter
    def duracion(self, valor: int):
        self.__duracion = valor if valor > 0 else 5
    
    @classmethod
    def mostrar_formatos(cls):
        super().mostrar_formatos()

    def comprimir_anuncio():
        print("COMPRESIÓN DE VIDEO NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio():
        print("RECORTE DE VIDEO NO IMPLEMENTADO AÚN")


class Display(Anuncio):
    FORMATO = "Display"
    SUB_TIPOS = ("tradicional", "native")

    def __init__(self, ancho: int, alto: int, url_archivo: str, url_click: str, sub_tipo: str) -> None:
        super().__init__(ancho, alto, url_archivo, url_click, sub_tipo)


    @classmethod
    def mostrar_formatos(cls):
        super().mostrar_formatos()

    def comprimir_anuncio():
        print("COMPRESIÓN DE ANUNCIOS DISPLAY NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio():
        print("REDIMENSIONAMIENTO DE ANUNCIOS DISPLAY NO IMPLEMENTADO AÚN")

class Social(Anuncio):
    FORMATO = "Social"
    SUB_TIPOS = ("facebook", "linkedin")
    def __init__(self, ancho: int, alto: int, url_archivo: str, url_click: str, sub_tipo: str) -> None:
        super().__init__(ancho, alto, url_archivo, url_click, sub_tipo)


    @classmethod
    def mostrar_formatos(cls):
        super().mostrar_formatos()

    def comprimir_anuncio():
        print("COMPRESIÓN DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio():
        print("REDIMENSIONAMIENTO DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADO AÚN")


if __name__ == "__main__":

    ##PRUEBAS##

    anuncio = Video("asdf", "asdf", "instream", -10)

    print(anuncio.ancho, anuncio.alto)

    anuncio.ancho = 0
    anuncio.alto = 3
    print(anuncio.ancho, anuncio.alto)


    anuncio.sub_tipo = "outstream"
    print(anuncio.sub_tipo)

    Video.mostrar_formatos()

    anuncio.duracion = 3
    print(anuncio.duracion)


    anuncio_display = Display(-1, 6, "asdf", "asdf", "facebookk")
    print(anuncio_display.ancho)
    print(anuncio_display.sub_tipo)
    anuncio_display.sub_tipo = "facebokk"




    # class Video(Anuncio):
    #     FORMATO = "Video"
    #     SUB_TIPOS = ("instream", "outstream")
    #     def __init__(self, url_archivo: str, url_click: str, sub_tipo: str, duracion: int) -> None:
    #         super().__init__(1, 1,  url_archivo, url_click, sub_tipo) # Ancho y alto fijos para la clase Video
    #         self.ancho = 1 #El problema es que si declaro esto aqui no se aplica el setter al crear la instancia, solo al modificarla
    #         self.alto = 1 #El problema es que si declaro esto aqui no se aplica el setter al crear la instancia, solo al modificarla
    #         self.duracion = duracion