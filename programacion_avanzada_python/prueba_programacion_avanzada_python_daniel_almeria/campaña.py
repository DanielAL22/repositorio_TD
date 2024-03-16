from anuncio import Video, Display, Social
from error import LargoExcedidoError

class Campaña:


    def __init__(self, nombre: str, fecha_inicio: str, fecha_termino: str) -> None:
        self.__nombre = nombre
        self.__fecha_inicio = fecha_inicio
        self.__fecha_termino = fecha_termino
        self.__listado_anuncios = []
        #self.anuncios_disponibles = ({"Video": Video, "Display": Display, "Social": Social})
        self.anuncios_disponibles = ["Video", "Display", "Social"]

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor: str):
        if len(valor) <= 250:
            self.__nombre = valor
        else:
            raise LargoExcedidoError("El número de carácteres excede lo permitido")


    @property
    def fecha_inicio(self):
        return self.__fecha_inicio

    @fecha_inicio.setter
    def fecha_inicio(self, valor: str):
        self.__fecha_inicio = valor

    @property
    def fecha_termino(self):
        return self.__fecha_termino

    @fecha_termino.setter
    def fecha_termino(self, valor: str):
        self.__fecha_termino = valor

    @property
    def listado_anuncios(self):
        return self.__listado_anuncios
    
    def crear_anuncio(self):
        tipo_anuncio = input("Ingrese el tipo de anuncio que desea crear ('Video', 'Display' o 'Social'):\n")
        while tipo_anuncio not in self.anuncios_disponibles:
            tipo_anuncio = input("Ingrese una de las opciones válidas('Video', 'Display' o 'Social'):\n")

        if tipo_anuncio == "Video":
            Video.mostrar_formatos()
            url_archivo = input("Ingrese la url del archivo:\n")
            url_click = input("Ingrese la url del click:\n")
            sub_tipo = input("Ingrese el subtipo del anuncio:\n")
            duracion = int(input("Ingrese la duración del video:\n"))

            nuevo_anuncio = Video(url_archivo, url_click, sub_tipo, duracion)
  

        elif tipo_anuncio == "Display":
            Display.mostrar_formatos()
            ancho = int(input("Ingrese el ancho del anuncio:\n"))
            alto = int(input("Ingrese el alto del archivo:\n"))
            url_archivo = input("Ingrese la url del archivo:\n")
            url_click = input("Ingrese la url del click:\n")
            sub_tipo = input("Ingrese el subtipo del anuncio:\n")


            nuevo_anuncio = Display(ancho, alto, url_archivo, url_click, sub_tipo)


        else:
            Social.mostrar_formatos()
            ancho = int(input("Ingrese el ancho del anuncio:\n"))
            alto = int(input("Ingrese el alto del archivo:\n"))
            url_archivo = input("Ingrese la url del archivo:\n")
            url_click = input("Ingrese la url del click:\n")
            sub_tipo = input("Ingrese el subtipo del anuncio:\n")


            nuevo_anuncio = Social(ancho, alto, url_archivo, url_click, sub_tipo)


        self.listado_anuncios.append(nuevo_anuncio)
        return nuevo_anuncio


    


    def __str__(self) -> str:
        num_videos = 0
        num_display = 0
        num_social = 0
        
        for anuncio in self.listado_anuncios:
            if anuncio.__class__.__name__ == "Video":
                num_videos += 1
            elif anuncio.__class__.__name__ == "Display":
                num_display += 1
            else:
                num_social += 1
        
        
        
        return f"""
        Nombre de la campaña: {self.nombre}
        Anuncios: {num_videos} Video, {num_display} Display, {num_social} Social
        """




if __name__ == "__main__":

    print("ESTAMOS EN CAMPAÑA")
    campaña = Campaña("asdf", "asdf", "asdf")
    campaña.crear_anuncio()

    print(len(campaña.listado_anuncios))
    print(campaña)

    campaña.crear_anuncio()

    print(len(campaña.listado_anuncios))
    print(campaña)

    campaña.crear_anuncio()

    print(len(campaña.listado_anuncios))
    print(campaña)



