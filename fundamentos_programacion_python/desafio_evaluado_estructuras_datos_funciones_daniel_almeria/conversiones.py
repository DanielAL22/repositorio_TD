import sys

_, tasa_sol, tasa_peso_argentino, tasa_dolar_americano, pesos_chilenos = tuple(sys.argv)



def calculo_tasa(tasa, monto):
    """Esta función convierte el monto introducido de CLP en otra moneda que se señale y redondea el resultado
    tasa: tasa de cambio de la moneda a la que queremos convertir
    monto: cantidad de CLP"""
    return round((float(tasa)) * int(monto), 1)


print(f'''
Los {pesos_chilenos} pesos equivalen a: 
{calculo_tasa(tasa_sol, pesos_chilenos)} Soles
{calculo_tasa(tasa_peso_argentino, pesos_chilenos)} Pesos Argentinos
{calculo_tasa(tasa_dolar_americano, pesos_chilenos)} Dólares
''')