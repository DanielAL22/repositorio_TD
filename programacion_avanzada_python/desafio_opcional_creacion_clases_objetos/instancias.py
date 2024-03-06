from te import Te

#Instancias de la clase Te
instancia_1 = Te()
instancia_2 = Te()

tipo_instancia_1 = type(instancia_1)
tipo_instancia_2 = type(instancia_2)

comparacion = tipo_instancia_1 == tipo_instancia_2


if comparacion == True:
    print("Ambos objetos son del mismo tipo")
else:
    print("Los objetos no son del mismo tipo”.")