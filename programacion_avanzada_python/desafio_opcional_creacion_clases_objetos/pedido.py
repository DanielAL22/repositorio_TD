from te import Te


te = Te()
tipo_te = int(input('''
Ingrese el tipo de te:
1: Corresponde a Té negro
2: Corresponde a Té verde
3: Corresponde a Agua de hierbas
'''))
formato_te = input('''
Ingrese el formato:
1: 300gr
2: 500gr
''')

te.set_nombre(nombre_te_num=tipo_te)

print(f"Sabor del té: {te.nombre}")

tiempo, recomendacion = Te.set_tiempo_recomendacion(nombre_te_num=tipo_te)
formato, precio = Te.set_formato_precio(formato_te_num=formato_te)


print(f"Formato: {formato} gr")
print(f"Precio: {formato}$")
print(f"Tiempo de preparación: {tiempo} minutos")
print(f"Recomendación: {recomendacion}")
print(f"Duración: {Te.duracion}")