import app.usuarios as usuarios

def requerimiento_1():
    users_data = []
    for pag in range(1,usuarios.obtener_total_paginas()+1):
        users_data += usuarios.obtener_usuarios(pag)
    return users_data

def requerimiento_2():
    usuario = {
        "name": "Ignacio",
        "job": "Profesor"
        }
    return usuarios.crear_usuario(usuario)


def requerimiento_3():
    #Creamos el usuario porque no existia
    usuario = {
        "name": "morpheus",
        "job": "zion resident"
        }
    usuarios.crear_usuario(usuario)

    actualizacion_usuario = {
        "name": "morpheus",
        "job": "zion resident",
        "residence": "zion"
        }

    return usuarios.actualizar_usuario(actualizacion_usuario, usuarios.buscar_id_usuario("morpheus", requerimiento_1()))

def requerimiento_4():
    nombre_usuario = "Tracey"
    id_usuario = usuarios.buscar_id_usuario(nombre_usuario, requerimiento_1())
    return usuarios.eliminar_usuario(id_usuario)


if __name__ == '__main__':

    print(requerimiento_1())
    print(len(requerimiento_1()))

    print(requerimiento_2())

    print(requerimiento_3())

    print(requerimiento_4())

    