import sys

precios = {'Notebook': 700000, 'Teclado': 25000, 'Mouse': 12000, 'Monitor': 250000, 'Escritorio': 135000, 'Tarjeta de Video': 1500000}



def filtro_precios():
    if len(sys.argv) == 2:
        umbral = int(sys.argv[1])
        resultado = {k:v for k,v in precios.items() if v > umbral}
        print(f'Los productos mayores al umbral son: {", ".join(resultado.keys())}')
    elif len(sys.argv) == 3 and (sys.argv[2]=='mayor' or sys.argv[2]=='menor'):
        umbral = int(sys.argv[1])
        mayor_menor = sys.argv[2]
        if sys.argv[2]=='mayor':
            resultado = {k:v for k,v in precios.items() if v > umbral}
        else:
            resultado = {k:v for k,v in precios.items() if v < umbral}
        print(f'Los productos {sys.argv[2]}es al umbral son: {", ".join(resultado.keys())}')

    else:
        print("Lo sentimos, no es una operación válida")

filtro_precios()




    
