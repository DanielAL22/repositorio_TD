from string import ascii_lowercase
from getpass import getpass

password = getpass('Ingrese la contraseña: ')



print(password)


intentos = 0
for letra_password in password:
    for letra_abc in ascii_lowercase:
        intentos += 1
        if letra_password == letra_abc:
            print(f'Letra adivinada: {letra_password} en el intento número {intentos}')
            
            break

print(f"La contraseña fue forzada en {intentos} intentos")
