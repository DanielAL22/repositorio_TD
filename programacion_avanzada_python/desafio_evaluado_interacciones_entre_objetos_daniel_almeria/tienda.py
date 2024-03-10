from abc import ABC, abstractmethod
from producto import Producto


class Tienda(ABC):
    def __init__(self, nombre_tienda: str, costo_delivery: int) -> None:
        super().__init__()
        self.nombre_tienda = nombre_tienda
        self.costo_delivery = costo_delivery
        self.listado_productos = []

    @abstractmethod
    def ingresar_producto(self, producto: Producto):  #COMPOSICION
        if producto in self.listado_productos:  
            for indice, prod in enumerate(self.listado_productos):
                if prod == producto:
                    self.listado_productos[indice].stock = prod + producto

            print("se actualizó el producto: ", producto)
        else: 
            self.listado_productos.append(producto)
            print("se añadio el producto: ", producto)

    @abstractmethod
    def listar_productos():
        pass

    @abstractmethod
    def realizar_venta(self, producto_solicitado: Producto, cantidad_requerida: int): #AGREGACIÓN
        stock = producto_solicitado.stock
        if (stock == 0) or (producto_solicitado not in self.listado_productos):
            print("El producto no existe o no hay stock disponible")
        else:
            if stock > cantidad_requerida:
                for indice, prod in enumerate(self.listado_productos):
                    if prod == producto_solicitado:
                        self.listado_productos[indice].stock = self.listado_productos[indice].stock - cantidad_requerida
                        print(f"Se vendieron {cantidad_requerida} unidades del producto {self.listado_productos[indice].nombre}. El stock restante es {self.listado_productos[indice].stock}")
            else:
                for indice, prod in enumerate(self.listado_productos):
                    if prod == producto_solicitado:
                        print(f"Se vendieron {self.listado_productos[indice].stock} unidades del producto {self.listado_productos[indice].nombre}. El stock restante es 0")
                        self.listado_productos[indice].stock = 0


class Restaurante(Tienda):
    STOCK_RESTAURANTE = 0
    def __init__(self, nombre_tienda: str, costo_delivery: int) -> None:
        super().__init__(nombre_tienda, costo_delivery)

    def ingresar_producto(self, producto: Producto):
        if producto.stock != 0:
            producto.stock = Restaurante.STOCK_RESTAURANTE
        if producto in self.listado_productos: 
            print("El producto ya existía: ", producto)
        else: 
            self.listado_productos.append(producto)
            print("se añadio el producto: ", producto)
    
    def listar_productos(self):
        encabezado = "NOMBRE || PRECIO"
        print(encabezado)
        print("-" * len(encabezado))
        for indice, _ in enumerate(self.listado_productos):
            print(f"{self.listado_productos[indice].nombre} || {self.listado_productos[indice].precio}")

    def realizar_venta(self, producto_solicitado: Producto, cantidad_requerida: int): #AGREGACIÓN
        if producto_solicitado not in self.listado_productos:
            print("El producto no existe")
        else:
            for indice, prod in enumerate(self.listado_productos):
                if prod == producto_solicitado:
                    print(f"Se vendieron {cantidad_requerida} unidades del producto {self.listado_productos[indice].nombre}")


class Supermercado(Tienda):
    def __init__(self, nombre_tienda: str, costo_delivery: int) -> None:
        super().__init__(nombre_tienda, costo_delivery)

    def ingresar_producto(self, producto: Producto):
        return super().ingresar_producto(producto)

    def listar_productos(self):
        encabezado = "NOMBRE || PRECIO || STOCK || OBSERVACIONES"
        print(encabezado)
        print("-" * len(encabezado))
        for indice, producto in enumerate(self.listado_productos):
            if producto.stock < 10:
                print(f"{self.listado_productos[indice].nombre} || {self.listado_productos[indice].precio} || {self.listado_productos[indice].stock} || Pocos productos disponibles")
            else:
                print(f"{self.listado_productos[indice].nombre} || {self.listado_productos[indice].precio} || {self.listado_productos[indice].stock}")

    def realizar_venta(self, producto_solicitado: Producto, cantidad_requerida: int):
        return super().realizar_venta(producto_solicitado, cantidad_requerida)


class Farmacia(Tienda):
    def __init__(self, nombre_tienda: str, costo_delivery: int) -> None:
        super().__init__(nombre_tienda, costo_delivery)

    @staticmethod
    def validar_cantidad(cantidad: int):
        if cantidad > 3:
            print("No está permitida la compra de más de tres productos por operación")
            return False
        return True

    def ingresar_producto(self, producto: Producto):
        return super().ingresar_producto(producto)

    def listar_productos(self):
        encabezado = "NOMBRE || PRECIO || OBSERVACIONES"
        print(encabezado)
        print("-" * len(encabezado))
        for indice, producto in enumerate(self.listado_productos):
            if producto.precio > 15000:
                print(f"{self.listado_productos[indice].nombre} || {self.listado_productos[indice].precio} || Envío gratis al solicitar este producto")
            else:
                print(f"{self.listado_productos[indice].nombre} || {self.listado_productos[indice].precio}")          

    def realizar_venta(self, producto_solicitado: Producto, cantidad_requerida: int):
        if self.validar_cantidad(cantidad_requerida) is True:
            return super().realizar_venta(producto_solicitado, cantidad_requerida)









