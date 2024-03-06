import sys

txt = sys.argv[1]



with open(txt, "r") as file: 
    texto=file.read()

n_caracteres_distintos = len(set(texto))
n_palabras_distintas = len(set(texto.split(" ")))


print(f"El número de caracteres distintos es: {n_caracteres_distintos}")
print(f"El número de palabras distintas es: {n_palabras_distintas}")

