
def factorial(numero):
    resultado = 1
    for numero in range(1,numero+1):
        resultado *= numero
    return resultado


def productoria(lista_numeros):
    resultado = 1
    for numero in lista_numeros:
        resultado *= numero
    return resultado

def calcular(**kwargs):
    for k,v in kwargs.items():
        if k[0] == 'f':
            print(f"El factorial de {v} es {factorial(v)}")
        if k[0] == 'p':
            print(f"La productoría de {v} es {productoria(v)}")


        
#Prueba
calcular(fact_1 = 5, prod_1 = [3,6,4,2,8], fact_2 = 6)







