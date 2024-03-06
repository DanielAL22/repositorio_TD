import math


print("Actividad 1 - Velocidad de escape")
print("-" * 100)

radio = float(input("Ingrese el radio en Kilómetros: "))*1000
constante = float(input("Introduce la constante g: "))

v_escape = math.sqrt(2 * constante * radio)

print("-" * 100)
print("-" * 100)

print(f"La velocidad de Escape es {round(v_escape, 1)} m/s")