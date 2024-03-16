from campaña import Campaña
from error import Error, LargoExcedidoError, SubTipoInvalidoError
from datetime import datetime



#crear campaña
nueva_campaña = Campaña("Nueva Campaña", "20/03/2024", "30/03/2024")
nuevo_anuncio = nueva_campaña.crear_anuncio()



log = None

try:
    #modificar campaña
    nuevo_nombre = input("Ingrese el nuevo nombre de la campaña:\n")
    nuevo_subtipo = input("Ingrese el nuevo subtipo para el anuncio:\n")
    nueva_campaña.nombre = nuevo_nombre
    nueva_campaña.listado_anuncios[nueva_campaña.listado_anuncios.index(nuevo_anuncio)].sub_tipo = nuevo_subtipo

except LargoExcedidoError as e:
    print(e)
    fecha_actual = datetime.now()
    with open(f'{str(fecha_actual).split(" ")[0]}.log', 'a') as log:
        log.write(f'{fecha_actual} - [ERROR]: {e}\n')

except SubTipoInvalidoError as e:
    print(e)
    fecha_actual = datetime.now()
    with open(f'{str(fecha_actual).split(" ")[0]}.log', 'a') as log:
        log.write(f'{fecha_actual} - [ERROR]: {e}\n')

except Error as e:
    print(e)
    fecha_actual = datetime.now()
    with open(f'{str(fecha_actual).split(" ")[0]}.log', 'a') as log:
        log.write(f'{fecha_actual} - [ERROR]: {e}\n')

finally:
    if log is not None:
        log.close()



print(nuevo_anuncio.sub_tipo)