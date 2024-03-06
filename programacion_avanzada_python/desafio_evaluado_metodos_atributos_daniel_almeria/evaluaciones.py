from pizza import Pizza



# 5.a. Usar la función print(), para que al ejecutar el script se muestre en pantalla los valores de los atributos de clase de la clase importada, sin crear una instancia de ella.
print("Tipo de ingredientes disponibles:", Pizza.tipo_ingrediente)
print("Tipos de masa disponibles:", Pizza.masa)
print("Precio:", Pizza.precio)
print("Tamaño:", Pizza.tamaño)

# 5.b. Usar la función print(), para que al ejecutar el script se muestre en pantalla si el elemento “salsa de tomate” se encuentra presente en la lista [“salsa de tomate", "salsa bbq"]. 
# Para ello use el método creado en el requerimiento 2, sin crear una instancia de la clase importada.
tipo_salsa =  ["salsa de tomate", "salsa bbq"]
print(Pizza.validar_elemento("salsa de tomate", tipo_salsa))

# 5.c. Crear una instancia de la clase importada, y luego llamar al método del requerimiento 3, para que al ejecutar el script se solicite ingredientes y tipo de masa al usuario.
pizza_1 = Pizza()
pizza_1.pedido()

# 5.d. Usar la función print(), para que al ejecutar el script, luego de que el usuario haya ingresado los ingredientes y tipo de masa, 
# se muestre en pantalla los ingredientes vegetales, el ingrediente proteico y el tipo de masa de la instancia creada en el paso anterior, y si esa instancia es una pizza válida o no.
print(f'''
Ingrediente proteico seleccionado: {pizza_1.seleccion_ingrediente_proteico}
Ingrediente vegetal 1 seleccionado: {pizza_1.seleccion_ingrediente_vegetal_1}
Ingrediente vegetal 2 seleccionado: {pizza_1.seleccion_ingrediente_vegetal_2}
Tipo de masa seleccionada: {pizza_1.seleccion_masa}
Validez del pedido: {pizza_1.validez_pedido}
''')