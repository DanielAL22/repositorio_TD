class Producto:
    def __init__(self, nombre: str, precio: int, stock: int = 0) -> None:
        self.__nombre = nombre
        self.__precio = precio
        self.stock = self.validar_stock(stock)

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre:str ):
        self.__nombre = self.nombre

    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, precio:str ):
        self.__precio = self.precio

    # @property
    # def stock(self):
    #     return self.__stock

    # @stock.setter
    # def stock(self, stock:int ):
    #     self.__stock = self.validar_stock(stock)

    def validar_stock(self, stock: int):
        if stock < 0:
            stock = 0
        return stock

    def __add__(self, other):
        return self.stock + other.stock

    def __sub__(self, other):
        return self.stock - other.stock

    def __eq__(self, other):
        return self.__nombre == other.__nombre







p = Producto("cafe", 2000, 5)

print(p.nombre)
print(p.stock)


