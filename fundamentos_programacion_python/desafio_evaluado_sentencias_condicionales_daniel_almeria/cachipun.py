import sys
import random


valores_posibles = ["piedra", "papel", "tijera"]
valor_usuario = sys.argv[1]
valor_cpu = random.choice(valores_posibles)




if valor_usuario not in valores_posibles:
    print("Argumento inválido: Debe ser piedra, papel o tijera.")
elif len(sys.argv) > 2:
    print("Por favor, introduce solo un valor a la vez")
else:
    if valor_cpu == valor_usuario:
        print(f"Tu jugaste {valor_usuario}")
        print(f"Computador jugó {valor_cpu}")
        print("Empate!!")
    elif (valor_usuario == "piedra" and valor_cpu == "papel") or (valor_usuario == "papel" and valor_cpu == "tijera") or (valor_usuario == "tijera" and valor_cpu == "piedra"):
        print(f"Tu jugaste {valor_usuario}")
        print(f"Computador jugó {valor_cpu}")
        print("Perdiste!!")
    else:
        print(f"Tu jugaste {valor_usuario}")
        print(f"Computador jugó {valor_cpu}")
        print("Ganaste!!")
