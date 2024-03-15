import json
from usuario import Usuario
from datetime import datetime


instancias_usuario = []
archivo_usuarios = None
log = None

try:
    with open("usuarios.txt") as archivo_usuarios:

        for line in archivo_usuarios:
            try:
                usuario = json.loads(line)
                nuevo_usuario = Usuario(usuario['nombre'], usuario['apellido'], usuario['email'], usuario['genero'])
                instancias_usuario.append(nuevo_usuario)
            except json.JSONDecodeError as e:
                fecha_actual = datetime.now()
                with open(f'{str(fecha_actual).split(" ")[0]}.log', 'a') as log:
                    log.write(f'{fecha_actual} - [ERROR]: {e}\n')
            except Exception as e:
                with open(f'{str(fecha_actual).split(" ")[0]}.log', 'a') as log:
                    log.write(f'{fecha_actual} - [ERROR]: {e}\n')
            finally:
                if log is not None:
                    log.close()


except FileNotFoundError as e:
    print("El archivo no existe", e)

finally: 
    if archivo_usuarios is not None:
        archivo_usuarios.close()



#prueba
for instancia in instancias_usuario:
    print(instancia)