import app.api_manager as api_manager


URL = "https://reqres.in/api/users"

def obtener_usuarios(n_pag:int = 1):
    response = api_manager.request_get(f"{URL}?page={n_pag}")['data']
    return response

def obtener_total_paginas():
    response = api_manager.request_get(URL)['total_pages']
    return response

def crear_usuario(usuario: dict):
    headers = {'Content-Type': 'application/json'}
    return api_manager.request_post(url=URL, headers=headers, payload=usuario)

def actualizar_usuario(update_usuario: dict, id: str):
    headers = {'Content-Type': 'application/json'}
    url = f"{URL}/{id}"
    return api_manager.request_put(url=url, headers=headers, payload=update_usuario)

def buscar_id_usuario(nombre_usuario:str, lista_usuarios:list):
    for usuario in lista_usuarios:
        if usuario['first_name'] == nombre_usuario:
            return usuario['id']
        else:
            "El usuario no fue encontrado"

def eliminar_usuario(id:int):
    headers = {'Content-Type': 'application/json'}
    url = f"{URL}/{id}"
    return api_manager.request_delete(url, headers=headers)







if __name__ == '__main__':
    url = "https://reqres.in/api/users"
    print(obtener_usuarios(1))
    print(obtener_usuarios(2))
    print(obtener_total_paginas())

    usuario = {
        "name": "morpheus",
        "job": "leader"
        }
    print(crear_usuario(usuario))

    actualizacion = {"residence": "zion"}
    print(actualizar_usuario(actualizacion, 2))

    lista_usuarios = [{'id': 11, 'email': 'george.edwards@reqres.in', 'first_name': 'George', 'last_name': 'Edwards', 'avatar': 'https://reqres.in/img/faces/11-image.jpg'}, 
    {'id': 12, 'email': 'rachel.howell@reqres.in', 'first_name': 'Rachel', 'last_name': 'Howell', 'avatar': 'https://reqres.in/img/faces/12-image.jpg'}]
    print(buscar_id_usuario('George', lista_usuarios))

    print(eliminar_usuario('George', lista_usuarios))

