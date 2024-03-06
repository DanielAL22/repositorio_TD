class Pizza:
    tipo_ingrediente = {'vegetal': ['tomate', 'aceitunas', 'champiñones'], 'proteico': ['pollo', 'vacuno', 'carne vegetal']}
    masa = ['tradicional', 'delgada']
    precio = 10000
    tamaño = 'familiar'

    @staticmethod
    def validar_elemento(elemento:str, lista_elementos:list):
        if elemento in lista_elementos:
            return True
        return False

    def pedido(self):
        self.seleccion_ingrediente_proteico = input("Ingrese su ingrediente proteico:\n")
        self.seleccion_ingrediente_vegetal_1 = input("Ingrese su primer ingrediente vegetal:\n")
        self.seleccion_ingrediente_vegetal_2 = input("Ingrese su segundo ingrediente vegetal:\n")
        self.seleccion_masa = input("Ingrese el tipo de masa:\n")

        if self.validar_elemento(self.seleccion_ingrediente_proteico, self.tipo_ingrediente['proteico']) and \
            self.validar_elemento(self.seleccion_ingrediente_vegetal_1, self.tipo_ingrediente['vegetal']) and \
            self.validar_elemento(self.seleccion_ingrediente_vegetal_2, self.tipo_ingrediente['vegetal']) and \
            self.validar_elemento(self.seleccion_masa, self.masa) is True:
                self.validez_pedido = True
        else:
            self.validez_pedido = False

        

        
