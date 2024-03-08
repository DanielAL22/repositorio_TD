from personaje import Personaje

print("¡Bienvenido a Gran Fantasía!")
nombre_personaje = input("Por favor indique nombre de su personaje:\n")
personaje_jugador = Personaje(nombre_personaje)
personaje_jugador.estado

personaje_rival = Personaje("Orco")
print("¡Oh no!, ¡Ha aparecido un Orco!")

personaje_jugador.probabilidad_ganar(personaje_rival)


eleccion_usuario = Personaje.aparicion_rival()

while eleccion_usuario == "1":
    personaje_jugador.pelea(personaje_jugador.probabilidad_ganar(personaje_rival), personaje_rival)


    eleccion_usuario = Personaje.aparicion_rival()


print("¡Has huido! El orco ha quedado atrás.")
