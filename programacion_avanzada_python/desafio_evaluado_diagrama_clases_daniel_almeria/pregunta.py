from alternativa import Alternativa

class Pregunta:
    def __init__(self, enunciado:str, es_requerida:bool, lista_alternativas:list, ayuda:str = None) -> None:
        self.enunciado = enunciado
        self.ayuda = ayuda
        self.es_requerida = es_requerida
        self.__lista_alternativas = lista_alternativas

    @property
    def lista_alternativas(self) -> list:
        return self.__lista_alternativas


    def mostrar_pregunta(self):
        if self.es_requerida == True:
            print(self.enunciado)
            if self.ayuda:
                print(self.ayuda)
                
            for alternativa in self.lista_alternativas:
                alternativa.mostrar_alternativa()

    

