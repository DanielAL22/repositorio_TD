import sys

peso = int(sys.argv[1])
altura = int(sys.argv[2])/100


imc = round(peso/(altura**2),2)


print(f"Su IMC es {imc}")
print("-"*100)


if imc < 18.5:
    print("La clasificación OMS es Bajo peso")
elif imc < 25:
    print("La clasificación OMS es Adecuado")
elif imc < 30:
    print("La clasificación OMS es Sobrepeso")
elif imc < 35:
    print("La clasificación OMS es Obesidad Grado I")
elif imc < 40:
    print("La clasificación OMS es Obesidad Grado II")
else:
    print("La clasificación OMS es Obesidad Grado III")