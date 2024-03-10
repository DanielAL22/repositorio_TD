from tienda import Restaurante, Supermercado, Farmacia
from producto import Producto



eleccion_establecimiento = input("""Bienvenido, ¿que tipo de establecimiento desea gestionar?
1. Restaurante
2. Supermercado
3. Farmacia
""")

def eleccion_operacion():
    eleccion = input("""¿Qúe desea hacer?
    1. Ingresar producto
    2. Listar productos
    3. Realizar venta
    0. Salir
    """)
    return eleccion


# Método para buscar un producto por nombre
def buscar_producto_por_nombre(nombre, lista_productos):
    for producto in lista_productos:
        if producto.nombre == nombre:
            return producto
    return None




if eleccion_establecimiento == "1":
    nombre_restaurante = input("Ingrese el nombre del restaurante:\n")
    precio_delivery = input("Ingrese el precio del delivery:\n")
    restaurante = Restaurante(nombre_restaurante, precio_delivery)
    eleccion = eleccion_operacion()

    while eleccion != 0:
        if eleccion == "1":
            print("INGRESO DE PRODUCTOS")
            nombre_inp = input("Ingrese el nombre del producto:\n")
            precio_inp = int(input("Ingrese el precio del producto:\n"))
            stock_inp = int(input("Ingrese el stock del producto:\n"))
            nuevo_producto = Producto(nombre_inp, precio_inp, stock_inp)
            restaurante.ingresar_producto(nuevo_producto)
        elif eleccion == "2":
            print("LISTADO DE PRODUCTOS")
            restaurante.listar_productos()
        elif eleccion == "3":
            print("VENTA DE PRODUCTOS")
            nombre_producto = input("Ingrese el nombre del producto:\n")
            cantidad = input("Ingrese la cantidad deseada:\n")
            restaurante.realizar_venta(buscar_producto_por_nombre(nombre_producto, restaurante.listado_productos), cantidad)
        else:
            "Nos vemos pronto"
            break
        eleccion = eleccion_operacion()


elif eleccion_establecimiento == "2":
    nombre_supermercado = input("Ingrese el nombre del supermercado:\n")
    precio_delivery = input("Ingrese el precio del delivery:\n")
    supermercado = Supermercado(nombre_supermercado, precio_delivery)
    eleccion = eleccion_operacion()

    while eleccion != 0:
        if eleccion == "1":
            print("INGRESO DE PRODUCTOS")
            nombre_inp = input("Ingrese el nombre del producto:\n")
            precio_inp = int(input("Ingrese el precio del producto:\n"))
            stock_inp = int(input("Ingrese el stock del producto:\n"))
            nuevo_producto = Producto(nombre_inp, precio_inp, stock_inp)
            supermercado.ingresar_producto(nuevo_producto)
        elif eleccion == "2":
            print("LISTADO DE PRODUCTOS")
            supermercado.listar_productos()
        elif eleccion == "3":
            print("VENTA DE PRODUCTOS")
            nombre_producto = input("Ingrese el nombre del producto:\n")
            cantidad = int(input("Ingrese la cantidad deseada:\n"))
            supermercado.realizar_venta(buscar_producto_por_nombre(nombre_producto, supermercado.listado_productos), cantidad)
        else:
            "Nos vemos pronto"
            break
        eleccion = eleccion_operacion()
else:
    nombre_farmacia = input("Ingrese el nombre de la farmacia:\n")
    precio_delivery = input("Ingrese el precio del delivery:\n")
    farmacia = Farmacia(nombre_farmacia, precio_delivery)
    eleccion = eleccion_operacion()

    while eleccion != 0:
        if eleccion == "1":
            print("INGRESO DE PRODUCTOS")
            nombre_inp = input("Ingrese el nombre del producto:\n")
            precio_inp = int(input("Ingrese el precio del producto:\n"))
            stock_inp = int(input("Ingrese el stock del producto:\n"))
            nuevo_producto = Producto(nombre_inp, precio_inp, stock_inp)
            farmacia.ingresar_producto(nuevo_producto)
        elif eleccion == "2":
            print("LISTADO DE PRODUCTOS")
            farmacia.listar_productos()
        elif eleccion == "3":
            print("VENTA DE PRODUCTOS")
            nombre_producto = input("Ingrese el nombre del producto:\n")
            cantidad = int(input("Ingrese la cantidad deseada:\n"))
            farmacia.realizar_venta(buscar_producto_por_nombre(nombre_producto, farmacia.listado_productos), cantidad)
        else:
            "Nos vemos pronto"
            break
        eleccion = eleccion_operacion()


